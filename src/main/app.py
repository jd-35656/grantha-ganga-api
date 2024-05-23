"""
Main flask app definition
"""

from flask import Flask

from src.main.config import Config
from src.main.routes import routes


def create_app(config: Config) -> Flask:
    """Creates flask app"""
    app = Flask("grantha-ganga-api")
    app.config.from_object(config)
    routes(app)
    return app
