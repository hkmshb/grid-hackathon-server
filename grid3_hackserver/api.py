from urllib.parse import urljoin
from flask import request, Blueprint
from flask_api.exceptions import NotFound

from .service import get_services
from .swagger import add_resources_doc
from .common import GRIDError, as_int, build_gsparams, include_paging_details


api_blueprint = apibl = Blueprint('', __name__)


class InvalidResourceError(GRIDError):
    """Exception thrown resources unknown to the server.
    """
    pass


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
        raise NotFound(detail=msgfmt.format(resource_name))

    gsparams = build_gsparams(request.args.copy())
    resultset = services[0](**gsparams)

    include_paging_details(gsparams, resultset)
    return resultset
