import os
import os.path as fs


BASE_DIR = fs.abspath(fs.dirname(__file__))


class BaseConfig:
    """Base configuration.
    """
    APP_NAME = os.getenv('APP_NAME', 'grid3-hackserver')


class DevConfig(BaseConfig):
    """Development configuration.
    """
    DEBUG = True


class ProdConfig(BaseConfig):
    """Production configuration.
    """
    DEBUT = False
