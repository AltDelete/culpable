from flask import Flask
from data import members

app = Flask(__name__)


@app.route("/senate")
def index():
    return members


if __name__ == "__main__":
    app.run(debug=True)
