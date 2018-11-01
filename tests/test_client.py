from grid3_hackserver.client import APIClient, GeoServerAPIClient



class TestClients:

    def test_build_url(self):
        client = APIClient('http://localhost:5000')
        f = client._build_url('schools', **{'gender': 'M'})
        assert f.url == 'http://localhost:5000/schools?gender=M'

    def test_gsclient_includes_provided_authkey(self):
        gsclient = GeoServerAPIClient('https://localhost:5000', '7782-038e2')
        f = gsclient._build_url('schools', **{'gender': 'M'})
        assert '&authkey=7782-038e2' in f.url
