import json
from urllib.parse import urljoin
from flask import request, Blueprint, Markup
from flask_api.exceptions import NotFound, ParseError

from .service import get_services
from .swagger import add_resources_doc
from .common import (
    GRIDError, as_int, build_gsparams, include_paging_details,
    extract_errorinfo
)


api_blueprint = apibl = Blueprint('', __name__)


class ServerError(GRIDError):
    """Exception thrown for server related error.
    """
    status_code = 500


@apibl.route('/', methods=['GET'])
def root_endpoint():
    url_root = request.url_root
    endpoints = {
        service.name: urljoin(url_root, service.name) + '/'
        for service in sorted(get_services(), key=lambda s: s.name)
    }
    return endpoints


@apibl.route('/favicon.ico/', methods=['GET'])
def sink_request():
    # sink requests for this resource
    return {}


@apibl.route('/<resource_name>/', methods=['GET'])
@add_resources_doc
def get_resources(resource_name):
    services = get_services(resource_name)
    if not services:
        msgfmt = 'Unknown resource requested: {}'
        raise NotFound(detail=Markup.unescape(msgfmt.format(resource_name)))

    gsparams = build_gsparams(request.args.copy())
    resp = services[0](**gsparams)

    try:
        resp.raise_for_status()
        resultset = resp.json()
    except json.decoder.JSONDecodeError:
        errmsg, status_code = extract_errorinfo(resp.text)
        if status_code >= 500:
            raise ServerError(detail=Markup.unescape(errmsg))
        raise ParseError(detail=Markup.unescape(errmsg))

    include_paging_details(gsparams, resultset)
    return resultset
