from flask import Flask
from api import api
from api import mongo
import settings



def create_app():
    """
    Create a flask app
    """
    # Init app
    app = Flask(__name__)
    app.config['MONGO_URI'] = settings.MONGO_URI
    api.init_app(app)

    return app



# MAIN
if __name__ == '__main__':

    # configs
    host = "0.0.0.0"
    port = "3000"

    app = create_app()
    app.run(host=host, port=port, debug=True)
