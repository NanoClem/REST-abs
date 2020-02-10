from setup import app
from api import register_api 
import settings


# REGISTER ALL API NAMESPACES
register_api(app)


if __name__ == '__main__':
    app.run(host= settings.HOST, port= settings.PORT, debug= settings.DEBUG)
