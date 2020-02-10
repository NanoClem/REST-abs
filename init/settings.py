import os

# Server
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = True

# MongoDB
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')
