from flask_restplus import Api
from .deal_namespace import ns as dealNS
from .mongo_init import mongo


# API constructor
api = Api(
    title = "REST_abs",
    description = "interact with data scraped from dealabs.com",
    version = 1.0
)

# Add namespace
api.add_namespace(dealNS)

# report our mongo instance
mongo = mongo
