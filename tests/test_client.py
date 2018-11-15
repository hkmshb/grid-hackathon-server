import pytest
from grid3_hackserver.common import APIClient, GeoServerAPIClient, CQLBuilder


cql_builder = CQLBuilder()


class TestClients:

    def test_build_url(self):
        client = APIClient('http://localhost:5000')
        f = client._build_url('schools', **{'gender': 'M'})
        assert f.url == 'http://localhost:5000/schools?gender=M'

    def test_gsclient_includes_provided_authkey(self):
        gsclient = GeoServerAPIClient('https://localhost:5000', '7782-038e2')
        f = gsclient._build_url('schools', **{'gender': 'M'})
        assert '&authkey=7782-038e2' in f.url


class TestQueryInterpreter:

    @pytest.mark.parametrize('args, expected', [
        (("state_code", "'KN'"), "state_code = 'KN'" ),
        (("client_age", "3"), "client_age = 3")
    ])
    def test_parse_simple_expr(self, args, expected):
        cond = cql_builder._parse_expr_simple(*args)
        assert cond == expected

    @pytest.mark.parametrize('args, expected', [
        (("state_code__like", "'KA%'"), "state_code LIKE 'KA%'"),
        (("state_name__ilike", "'KA%'"), "state_name ILIKE 'KA%'"),
        (("client_age__lt", "20"), "client_age < 20"),
        (("client_age__le", "20"), "client_age <= 20"),
        (("client_age__gt", "20"), "client_age > 20"),
        (("client_age__ge", "20"), "client_age >= 20"),
        (("client_age__in", "20,23,24"), "client_age IN (20, 23, 24)"),
        (("client_age__between", "20,25"), "client_age BETWEEN 20 AND 25"),
    ])
    def test_parse_complex_expr(self, args, expected):
        cond = cql_builder._parse_expr_complex(*args)
        assert cond == expected

    def test_parse(self):
        cql = cql_builder({
            "state_code__like": "'KA%'",
            "client_age__in": "20,55,73"
        })
        assert cql == "state_code LIKE 'KA%' AND client_age IN (20, 55, 73)"
