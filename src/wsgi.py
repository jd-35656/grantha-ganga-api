"""Entry point for flask app"""

from src.main.app import create_app
from src.main.config import Config

config = Config()

application = create_app(config=config)
