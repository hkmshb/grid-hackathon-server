import os
from flask_api import FlaskAPI


def get_version():
    '''Retrieve and return version details.
    '''
    import pkg_resources
    package = pkg_resources.require('grid3_hackserver')
    return package[0].version


def create_app(script_info=None):
    # create app & set config
    app = FlaskAPI(__name__)

    default_app_setting = 'grid3_hackserver.config.DevConfig'
    app_settings = os.getenv('APP_SETTINGS', default_app_setting)
    app.config.from_object(app_settings)

    # register all service endpoints
    from . import resource

    # register blueprints
    from .api import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
