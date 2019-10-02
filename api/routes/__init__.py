import os.path
import markdown
from flask import Flask, request, abort

# Instance of Flask
app = Flask(__name__)


#=============================================================
#   INDEX
#=============================================================
@app.route("/")
def index():
    """Showing the API doc file"""
    with open(os.path.dirname(app.root_path) + "/README.md", "r") as doc_file :
        content = doc_file.read()
        return markdown.markdown(content)


#=============================================================
#   CRUD
#=============================================================

# CREATE A DATA COLLECTION
@app.route("/deal", methods=['POST'])
def createData():
    """Create a new data collection"""
    if request.method == 'POST' :
        return "data collection successfuly created", 201

#-------------------------------------------------------

# READ ALL STORED DATA
@app.route("/deals", methods=['GET'])
def getAllData():
    """Showing all stored deals"""
    return {'message': 'success', 'data': {}}, 200

# READ A DATA COLLECTION FROM AN ID
@app.route("/deal/<int:id>", methods=['GET'])
def getDataByID(id):
    """Return a data collection from an id"""
    return {'message': 'success', 'data': {}}, 200

#-------------------------------------------------------

# UPDATE A DATA COLLECTION
@app.route("/deal", methods=['PUT'])
def updateData():
    """Update a data collection"""
    if request.method == "PUT" :
        return "Data collection successfuly updated", 204

#-------------------------------------------------------

# DELETE A DATA COLLECTION
@app.route("/deal", methods=['DELETE'])
def deleteData():
    """Delete a data collection"""
    if request.method == "DELETE" :
        return "Data collection successfuly deleted", 204
