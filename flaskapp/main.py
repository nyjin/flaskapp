from flask import Flask
from config import Config
from flaskapp.extensions import db, migrate, ma
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)


def create_app(config_obj=Config):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    init_app(app)
    return app


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from flaskapp.resource import api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/v1")
