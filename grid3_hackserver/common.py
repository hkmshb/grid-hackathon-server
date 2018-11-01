import enum
import json
import requests
from furl import furl

# singleton instance ref; this is set when the flask
# app is being created in grid3_hackserver.create_app
config = None


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
        ('version', '1.0.0'),
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
