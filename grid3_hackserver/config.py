import os
import os.path as fs


def getenv(key):
    """Get an environment variable and raises an exception if none is found.
    """
    val = os.getenv(key)
    if not val:
        msgfmt = 'Required environment variable not set: {}'
        raise Exception(msgfmt.format(key))
    return val


class BaseConfig:
    """Base configuration.
    """
    APP_NAME = os.getenv('APP_NAME', 'grid3-hackserver')
    GEOSERVER_URLBASE = getenv('G3H_GEOSERVER_URLBASE')
    GEOSERVER_AUTHKEY = getenv('G3H_GEOSERVER_AUTHKEY')


class DevConfig(BaseConfig):
    """Development configuration.
    """
    DEBUG = True


class ProdConfig(BaseConfig):
    """Production configuration.
    """
    DEBUG = False
