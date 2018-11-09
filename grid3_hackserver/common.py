import enum
import json
import requests
from furl import furl
from flask import request
from .config import as_bool, as_int
from collections import namedtuple


# singleton instance ref; this is set when the flask
# app is being created in grid3_hackserver.create_app
config = None


class GRIDError(Exception):
    """Base exception for all GRID related errors.
    """
    pass


def build_gsparams(reqparams):
    """Transforms query params as understood by the proxy server to one
    understood by GeoServer.

    :param reqparams: request query parameters.
    :type reqparams:
    """
    gsparams = {}

    # handling pagination; disable when size less than 1
    can_paginate = as_bool(config.ENABLE_PAGINATION, False)
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

    # apply left-over reqparams as is
    gsparams.update(reqparams)
    return gsparams


def include_paging_details(gsparams, resultset):
    """Updates resultset retrieved from GeoServer with pagination details.

    :param gsparams: parameters used by GeoServer to generate resultset.
    :param resultset: response returned by GeoServer for gsparams.
    """
    can_paginate = as_bool(config.ENABLE_PAGINATION, False)
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
            resp = requests.get(furlobj.url, headers=request_headers)
        else:
            payload = payload or {}
            request_url = self._build_url(urlpath)
            resp = request.post(furlobj.url, headers=request_headers,
                                data=json.dumps(payload))

        resp.raise_for_status()
        return resp.json()

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
