from flask import Flask
from api import api


if __name__ == '__main__':

    # configs
    host = "0.0.0.0"
    port = "3000"

    # Init app
    app = Flask(__name__)
    api.init_app(app)

    app.run(host=host, port=port, debug=True)
