"""
Main flask app definition
"""

from typing import Dict

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index() -> Dict:
    """Demo

    Returns:
        Dict: demo
    """
    return {
        "health": "working",
    }
