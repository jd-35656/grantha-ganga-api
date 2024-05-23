"""Demo blueprint"""

from typing import Dict

from flask import Blueprint

blp = Blueprint("demo", __name__)


@blp.route("/")
def index() -> Dict:
    """Demo
    Returns:
        Dict: demo
    """
    return {
        "health": "working",
    }
