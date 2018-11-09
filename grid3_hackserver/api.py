from urllib.parse import urljoin
from flask import request, Blueprint
from .service import get_services
from .swagger import add_resources_doc


api_blueprint = apibl = Blueprint('', __name__)


@apibl.route('/', methods=['GET'])
def root_endpoint():
    url_root = request.url_root
    endpoints = {
        service.name: urljoin(url_root, service.name) + '/'
        for service in get_services()
    }
    return endpoints


@apibl.route('/<resource_name>/', methods=['GET'])
@add_resources_doc
def get_resources(resource_name):
    services = get_services(resource_name)
    if not services:
        raise Exception('404 Not Found')

    # NOTE: test_qs is being used pending when
    # pagination is implemented ...
    test_qs = {'maxFeatures': 1}
    return services[0](**test_qs)
