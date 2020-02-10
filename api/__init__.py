from flask_restplus import Api
from .deal_namespace import ns as dealNS



# API constructor
api = Api(
    title = "REST_abs",
    description = "interact with data scraped from dealabs.com",
    version = 1.0
)

# REGISTER
def register_api(app):
    """
    Add namespaces and register api for app
    """
    api.add_namespace(dealNS)
    api.init_app(app)
