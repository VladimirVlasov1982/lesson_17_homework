from flask import Flask
from models import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False
    db.init_app(app)
    return app
