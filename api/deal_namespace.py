from flask_restplus import Namespace, Resource, fields
from datetime import datetime
from init.setup import db

# ns var and Metadata about the namespace
ns = Namespace('api/deals', description = 'Deals related operations')



#=============================================================
#   MODEL
#=============================================================

# TEMPLATE
deal_model = ns.model('Deal', {
    "id"         : fields.Integer(readonly=True, description="The deal unique identifier"),
    "url"        : fields.String(required=True, description="The deal url"),
    "created at" : fields.String(required=True, description="Date of creation")
    })


# DAO class Object
class DealModel(object):
    """
    """
    def getAll(self):
        """
        Return all data collections
        """
        return db.find()


    def get(self, id):
        """
        Return data from a deal
        """
        data = db.deals.find_one({'id': id})
        return data


    def create(self, data):
        """
        Create a new data collection
        """
        data['created_at'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        db.insert_one(data)
        return data


    def update(self, id, data):
        """
        Update a data collection
        """
        db.update_one({'id': id}, data)
        return data


    def delete(self, id):
        """
        Delete a data collection
        """
        db.delete_one({'id': id})


# DAO object
DAO = DealModel()



#=============================================================
#   ROUTING
#=============================================================

#---------------------------------------------
#   DATA LIST
#---------------------------------------------
@ns.route("/", strict_slashes = False)     # strict_slashes setted to False so the debuger ignores it
class DataList(Resource):
    """
    Get a list of all stored data and allows POST to add new datasets
    """

    @ns.doc('list_deals')
    @ns.marshal_list_with(deal_model)
    def get(self):
        """
        Return a list of all deals
        """
        return DAO.getAll(), 200


    @ns.doc('create_deal')
    @ns.expect(deal_model)
    @ns.marshal_with(deal_model, code=201)
    def post(self):
        """
        Create a new deal
        """
        return DAO.create(ns.payload), 201


#---------------------------------------------
#   CRUD
#---------------------------------------------
@ns.route("/<int:id>")
@ns.response(404, 'Deal not found')
@ns.param('id', 'The deal unique identifier')
class Data(Resource):
    """
    Show a single data item, update one, or delete one
    """

    @ns.doc('get_deal')
    @ns.marshal_with(deal_model)
    def get(self, id):
        """
        Return a single data collection
        """
        return DAO.get(id), 200


    @ns.doc('update_deal')
    @ns.marshal_with(deal_model)
    def put(self, id):
        """
        Update a data collection
        """
        return DAO.update(id, ns.payload), 204


    @ns.doc('delete_deal')
    @ns.response(204, 'Deal deleted')
    def delete(self, id):
        """
        Delete a data collection
        """
        DAO.delete(id)
        return '', 204
