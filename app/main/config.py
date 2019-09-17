import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'pls_put_secret_key')
    DEBUG = False
    CSRF_ENABLED = True


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:student@localhost/enotice'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')


config_factory = dict(
    dev=DevConfig,
    prod=ProdConfig
)

key = Config.SECRET_KEY
