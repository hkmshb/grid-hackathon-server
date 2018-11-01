import os
from flask_api import FlaskAPI


REQUIRED_ENVVARS = (
    'G3H_GEOSERVER_URLBASE',
    'G3H_GEOSERVER_AUTHKEY'
)


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

    # include GH3 env vars
    for varname in REQUIRED_ENVVARS:
        value = os.getenv(varname, None)
        if not value:
            msgfmt = "Environment variable not set: '{}'"
            raise Exception(msgfmt.format(varname))
        app.config[varname] = (value or '').strip()

    # register all service endpoints
    from . import resource

    # register blueprints
    from .api import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
