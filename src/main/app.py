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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
