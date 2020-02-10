from flask import Flask
from flask_pymongo import PyMongo
import settings


# INSTANCIATE OUR APP
def create_app():
    """
    Create a flask app
    """
    # Init app
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/dealsDB' #settings.MONGO_URI
    app.config['MONGO_DBNAME'] = settings.MONGO_DBNAME

    return app


# APP OBJECT
app = create_app()

# mongoDB object
db = PyMongo(app)
