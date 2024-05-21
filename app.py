from typing import Dict

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index() -> Dict:
    return {
        "health": "working",
    }


if __name__ == "__main__":
    app.run()
