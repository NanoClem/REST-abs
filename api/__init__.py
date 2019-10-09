from flask_restplus import Api
from .deal_namespace import api as dealNS


# API constructor
api = Api(
    title = "REST_abs",
    description = "interact with data scraped from dealabs.com",
    version = 1.0
)

# Add namespace
api.add_namespace(dealNS)
