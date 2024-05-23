"""Route integration"""

from flask import Flask

from src.main.blp import blp


def routes(app: Flask) -> None:
    """Register routes"""

    app.register_blueprint(
        blueprint=blp,
    )
