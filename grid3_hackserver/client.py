import furl
import requests


class APIClient:
    """Defines base interfaces expected for a client interacting with 
    external services.
    """

    def __init__(self, base_url):
        self.base_url = base_url


class GeoServerAPIClient(APIClient):
    """Defines the interfaces to ease interacting with a GeoServer instance.
    """
    DEFAULT_HEADERS = (
        (),
    )

    def __init__(self, base_url, authkey):
        super().__init__(base_url)
        self.authkey = authkey

    def get(self, **params):
        pass

    def post(self, **params):
        pass
