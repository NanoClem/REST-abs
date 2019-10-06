import os.path
import markdown
from flask import Flask, request, make_response

# Instance of Flask
app = Flask(__name__)


#=============================================================
#   INDEX
#=============================================================
@app.route("/")
def index():
    """Showing the API doc file"""
    with open(os.path.dirname(app.root_path) + "../../README.md", "r") as doc_file :
        content = doc_file.read()
        return markdown.markdown(content)

#=============================================================
#   ERROR HANDLERS
#=============================================================
@app.errorhandler(404)
def not_found(error):
    """Handle 404 error with a JSON response"""
    return make_response({'message': 'error not found', 'data': {}}, 404)

@app.errorhandler(405)
def not_allowed(error):
    """Handle 405 error with a JSON response"""
    return make_response({'message': 'method not allowed', 'data': {}}, 405)


#=============================================================
#   CRUD
#=============================================================

# CREATE A DATA COLLECTION
@app.route("/deal", methods=['POST'])
def createData():
    """Create a new data collection"""
    if request.method == 'POST' :
        return {'message': 'success', 'data': {}}, 201

#-------------------------------------------------------

# READ ALL STORED DATA
@app.route("/deals", methods=['GET'])
def getAllData():
    """Showing all stored deals"""
    return {'message': 'success', 'data': {}}, 200

# READ A DATA COLLECTION FROM AN ID
## TODO : abort with 404 error when not found in database
@app.route("/deal/<int:id>", methods=['GET'])
def getDataByID(id):
    """Return a data collection from an id"""
    return {'message': 'success', 'data': {}}, 200

#-------------------------------------------------------

# UPDATE A DATA COLLECTION
@app.route("/deal/<int:id>", methods=['PUT'])
def updateData(id):
    """Update a data collection"""
    if request.method == "PUT" :
        return '', 204

#-------------------------------------------------------

# DELETE A DATA COLLECTION
@app.route("/deal/<int:id>", methods=['DELETE'])
def deleteData(id):
    """Delete a data collection"""
    if request.method == "DELETE" :
        return '', 204
