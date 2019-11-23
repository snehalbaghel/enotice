import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'pls_put_secret_key')
    DEBUG = False
    CSRF_ENABLED = True


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:student@localhost/enotice'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')


config_factory = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=ProdConfig
)

key = Config.SECRET_KEY
