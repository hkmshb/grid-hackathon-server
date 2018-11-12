import os
import os.path as fs


TRUTHY = ('true', 't', 'yes', 'y', '1')
FALSEY = ('false', 'f', 'no', 'n', '0')


def as_bool(value, default):
    """Converts a number or string value to a boolean, if conversion fails
    the provided default is returned.
    """
    if isinstance(value, bool):
        return value

    value = str(value).lower()
    if value in TRUTHY:
        return True
    if value in FALSEY:
        return False
    return default


def as_int(value, default):
    """Converts a number or string to an integer if conversion fails the
    provided default is returned.
    """
    try:
        return int(value)
    except ValueError:
        return int(default)


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
    PAGINATION_ENABLED = as_bool(getenv('G3H_PAGINATION_ENABLED'), False)
    DEFAULT_PAGESIZE = as_int(getenv('G3H_DEFAULT_PAGESIZE'), 500)

    # rate limit configs
    RATELIMIT_ENABLED = as_bool(getenv('G3H_RATELIMIT_ENABLED'), True)
    RATELIMIT_DEFAULT = getenv('G3H_RATELIMIT_DEFAULT')


class DevConfig(BaseConfig):
    """Development configuration.
    """
    DEBUG = True


class ProdConfig(BaseConfig):
    """Production configuration.
    """
    DEBUG = False
