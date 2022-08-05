from typing import Type
from flask import Flask

from config import BaseConfig


def create_app(config: Type[BaseConfig]):
    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False

    return app
