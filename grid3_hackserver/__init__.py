import os
import logging
from werkzeug.utils import import_string
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter
from flask_api import FlaskAPI
from flasgger import Swagger
from . import common


def get_version():
    '''Retrieve and return version details.
    '''
    import pkg_resources
    package = pkg_resources.require('grid3_hackserver')
    return package[0].version


def create_app(script_info=None):
    configure_logging()

    # create app & set config
    app = FlaskAPI(__name__)
    app.config['SWAGGER'] = {
        'title': 'Grid Hackathon',
        'specs_route': '/docs',
        'uiversion': 3
    }
    swagger = Swagger(app)

    default_app_setting = 'grid3_hackserver.config.DevConfig'
    app_settings = os.getenv('APP_SETTINGS', default_app_setting)

    common.config = import_string(app_settings)
    app.config.from_object(common.config)

    # register all service endpoints
    from . import resource

    # register blueprints
    from .api import api_blueprint, root_endpoint
    app.register_blueprint(api_blueprint)

    # configure rate limiting
    limiter = Limiter(app, key_func=get_remote_address)
    limiter.exempt(root_endpoint)

    # alter some settings if production env
    if not common.config.DEBUG:
        app.config['DEFAULT_RENDERERS'] = [
            'flask_api.renderers.JSONRenderer'
        ]

    configure_errorhandlers(app)
    return app


def configure_logging():
    """Configures the logging for the app.
    """
    logging.basicConfig(
        level=os.environ.get('G3H_LOGGING_LEVEL', logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


def configure_errorhandlers(app):
    from flask import jsonify, make_response

    @app.errorhandler(429)
    def ratelimit_handler(e):
        return make_response(
            jsonify(message="Ratelimit exceeded. {}".format(e)),
            429
        )

    @app.errorhandler(404)
    def resource_not_found(e):
        return make_response(
            jsonify(message="Resource not found. {}".format(e)),
            404
        )
