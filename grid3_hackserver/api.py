from urllib.parse import urljoin
from flask import request, Blueprint
from .service import get_services


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
def get_resources(resource_name):
    return {
        'resource_name': resource_name
    }
