from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS


from .config import config_factory

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_key):
    app = Flask(__name__, static_folder="static")
    app.config.from_object(config_factory[config_key])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    CORS(app, origins="http://localhost:8080",
        allow_headers=['Content-Type', 'Authorization'],
        methods=['GET', 'POST', 'OPTIONS'])
    # app.config['CORS_HEADERS'] = 'Content-Type'

    return app
