from flask import Blueprint


api_blueprint = apibl = Blueprint('', __name__)


@apibl.route('/', methods=['GET'])
def root_endpoint():
    return {
    }
