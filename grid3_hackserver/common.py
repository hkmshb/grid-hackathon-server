import enum
import json
import logging
import requests
from collections import namedtuple

from furl import furl
from flask import request
from flask_api.exceptions import APIException

from .config import as_bool, as_int

# singleton instance ref; this is set when the flask
# app is being created in grid3_hackserver.create_app
config = None

logger = logging.getLogger(__name__)


class GRIDError(APIException):
    """Base exception for all GRID related errors.
    """
    pass


class CQLBuilder:
    OP_MARKER = '__'
    CMP_OPERATORS = ('lt', 'le', 'gt', 'ge')
    ALL_OPERATORS = CMP_OPERATORS + ('like', 'ilike', 'in', 'between')

    def __init__(self):
        pass

    def __call__(self, reqparams):
        conditions = []
        for (expr, val) in reqparams.items():
            if self.OP_MARKER in expr:
                cql_cond = self._parse_expr_complex(expr, val)
            else:
                cql_cond = self._parse_expr_simple(expr, val)
            conditions.append(cql_cond)
        return ' AND '.join(conditions)

    def _build_cmp_expr(self, field, op, value):
        cond_fmt = '{field} {op} {value}'
        kw = {'field': field, 'value': value, 'op': None}
        if op == 'lt':
            kw['op'] = '<'
        elif op == 'le':
            kw['op'] = '<='
        elif op == 'gt':
            kw['op'] = '>'
        elif op == 'ge':
            kw['op'] = '>='
        return cond_fmt.format(**kw)

    def _build_term_expr(self, field, op, value):
        if 'like' in op:
            cond = '{field} {op} {value}'.format(
                field=field, op=op.upper(), value=value
            )
        elif op == 'in':
            values = [v.strip() for v in value.split(',')]
            value = '({})'.format(', '.join(values))
            cond = '{field} IN {value}'.format(field=field, value=value)
        elif op == 'between':
            values = [v.strip() for v in value.split(',')]
            if len(values) != 2:
                errmsg = "Invalid 'BETWEEN' query expression: {}"
                raise GRIDError(errmsg.format(field + '__' + op + '=' + value))

            cond = '{field} BETWEEN {lt} AND {rt}'.format(
                field=field, lt=values[0], rt=values[1]
            )
        return cond

    def _parse_expr_simple(self, expr, value):
        return "{} = {}".format(expr, value)

    def _parse_expr_complex(self, expr, value):
        field, op = expr.split(self.OP_MARKER)
        if op not in self.ALL_OPERATORS:
            raise GRIDError('Invalid query expression')

        return (
            self._build_cmp_expr(field, op, value)
            if op in self.CMP_OPERATORS else
                self._build_term_expr(field, op, value)
        )


# singleton instance 
cql_builder = CQLBuilder()


def build_gsparams(reqparams):
    """Transforms query params as understood by the proxy server to one
    understood by GeoServer.

    :param reqparams: request query parameters.
    :type reqparams:
    """
    gsparams = {}

    # handling pagination; disable when size less than 1
    can_paginate = as_bool(config.PAGINATION_ENABLED, False)
    if can_paginate:
        size = as_int(reqparams.pop('size', ''), config.DEFAULT_PAGESIZE)
        if size > 0:
            page = as_int(reqparams.pop('page', ''), 1)
            gsparams.update({
                'count': size,
                'startIndex': (size * (page - 1)) + 1,
            })

    # ensure result are always sorted
    gsparams.update({'sortBy': reqparams.pop('sort_by', 'global_id')})

    # restrict result fields if fields specified
    fields = reqparams.pop('fields', None)
    if fields:
        gsparams.update({'propertyName': fields})

    # extract and use cql query arg if present and pass through as is
    # or build from whatever args are left over in 'reqparams'
    cql = reqparams.pop('cql', None)
    if not cql:
        cql = cql_builder(reqparams)

    if cql:
        gsparams.update({'cql_filter': cql})
    return gsparams


def include_paging_details(gsparams, resultset):
    """Updates resultset retrieved from GeoServer with pagination details.

    :param gsparams: parameters used by GeoServer to generate resultset.
    :param resultset: response returned by GeoServer for gsparams.
    """
    can_paginate = as_bool(config.PAGINATION_ENABLED, False)
    if not can_paginate:
        return resultset

    size, page = (0, 0)
    try:
        size = as_int(gsparams.get('count', ''), 0)
        start_idx = as_int(gsparams.get('startIndex', ''), 0)
        page = int(((start_idx - 1) / size) + 1)
    except ValueError:
        pass

    total_feat_count = resultset.get('totalFeatures', 0)
    page_feat_count = len(resultset.get('features', []))

    total_pages = int(total_feat_count / size) + 1
    prev_page = (page - 1) if page > 1 else 1
    next_page = min((page + 1), total_pages)

    prev_furl = furl(request.url)
    prev_furl.args['page'] = prev_page

    next_furl = prev_furl.copy()
    next_furl.args['page'] = next_page

    page = min(page, total_pages)
    resultset['pager'] = pager = {}

    if page > prev_page:
        pager['prev'] = prev_furl.url
    if page < next_page:
        pager['next'] = next_furl.url


def extract_errorinfo(xmlval):
    """Extract and return error text from xml value.
    """
    import re
    from xml.etree import ElementTree

    root = ElementTree.fromstring(xmlval)
    namespaces = {'ows': 'http://www.opengis.net/ows/1.1'}

    exc_elem = root.find('ows:Exception/ows:ExceptionText', namespaces)
    if exc_elem is None:
        errmsg = 'Unknown server error occured due to invalid request.'
        logger.error(
            errmsg + ' Unrecognized non-JSON GeoServer response provided: %s',
            xmlval
        )
        return (errmsg, 500)

    # mask geoserver layer info
    exc_text = exc_elem.text
    match = re.findall('GRID\w+:\w+', exc_text)
    for m in match:
        exc_text = exc_text.replace(m, '***')
    return (exc_text, 400)


class OGCServiceType(enum.Enum):
    """Defines the subset of OGC service types that are proxied from GeoServer.
    """
    WFS = 'Web Features Service'
    WMS = 'Web Map Service'


class APIClient:
    """Defines base interfaces expected for a client interacting with 
    external services.
    """
    DEFAULT_HEADERS = (
    )

    def __init__(self, urlbase, apikey=None):
        if '://' not in urlbase or urlbase.startswith('://'):
            raise ValueError('urlbase must specify a scheme')

        if urlbase and urlbase.endswith('/'):
            urlbase = urlbase[:-1]

        self.urlbase = urlbase
        self.apikey = apikey

    def _build_url(self, urlpath=None, **params):
        furlobj = furl(self.urlbase, path=urlpath, args=params)
        return furlobj

    def __call__(self, urlpath=None, payload=None, headers=None, as_get=True):
        """Performs a request to an external service.

        A GET request is made by default if as_get remains True and payload is
        treated as the query params otherwise a POST request is made if as_get
        is False.
        """
        request_headers = dict(self.DEFAULT_HEADERS)
        request_headers.update(headers or {})

        if as_get:
            furlobj = self._build_url(urlpath, **payload)
            logger.info(f"proxy target: {furlobj.url}")
            resp = requests.get(furlobj.url, headers=request_headers)
        else:
            payload = payload or {}
            request_url = self._build_url(urlpath)
            logger.info(f"proxy target: {furlobj.url}")
            resp = request.post(furlobj.url, headers=request_headers,
                                data=json.dumps(payload))
        return resp

    def __repr__(self):
        """Returns a string representation for instances.
        """
        fmt = '<APIClient (urlbase={}, apikey=***)>'
        return fmt.format(self.urlbase)


class GeoServerAPIClient(APIClient):
    """Defines the interfaces to ease interacting with a GeoServer instance.
    """
    DEFAULT_QUERYPARAMS = (
        ('version', '2.0.0'),
        ('request', 'GetFeature'),
        ('outputFormat', 'application/json'),
        ('service', OGCServiceType.WFS.name),
    )

    def _build_url(self, urlpath, **params):
        qry_params = dict(self.DEFAULT_QUERYPARAMS)
        qry_params.update(params)

        keyname = 'authkey'
        furlobj = super()._build_url(urlpath, **qry_params)
        if self.apikey and keyname not in furlobj.args:
            furlobj.args[keyname] = self.apikey
        return furlobj
