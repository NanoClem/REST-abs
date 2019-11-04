from flask_restplus import Namespace, Resource, fields
from datetime import datetime

# ns var and Metadata about the namespace
ns = Namespace('api/deals', description = 'Deals related operations')



#=============================================================
#   MODEL
#=============================================================

# TEMPLATE
deal = ns.model('Deal', {
    "id"  : fields.Integer(readonly=True, description="The deal unique identifier"),
    "url" : fields.String(required=True, description="The deal url"),
    "date" : datetime.now()
    })


# DAO class Object
class DealModel(object):
    """
    """

    def __init__(self):
        """ """
        self.deals = []   ## TEMP: temporary database for tests
        self.cpt   = 0    ## TEMP: temporary way to give id


    def get(self, id):
        """Return data from a deal"""
        for deal in self.deals:
            if deal['id'] == id:
                return deal
        ns.abort(404, "Deal {} doesn't exist".format(id), data={})


    def create(self, data):
        """Create a new data collection"""
        try:
            deal = data
            deal['id'] = self.cpt = self.cpt + 1
            self.deals.append(deal)
        except TypeError as e:
            print("Error {}".format(e))
        return deal


    def update(self, id, data):
        """Update a data collection"""
        deal = self.get(id)
        deal.update(data)
        return deal


    def delete(self, id):
        """Delete a data collection"""
        deal = self.get(id)
        self.deals.remove(deal)


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
    @ns.marshal_list_with(deal)
    def get(self):
        """Return a list of deals"""
        return DAO.deals, 200

    @ns.doc('create_deal')
    @ns.expect(deal)
    @ns.marshal_with(deal, code=201)
    def post(self):
        """Create a new deal"""
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
    @ns.marshal_with(deal)
    def get(self, id):
        """Return data about a deal"""
        return DAO.get(id), 200

    @ns.doc('update_deal')
    @ns.marshal_with(deal)
    def put(self, id):
        """Update a data collection"""
        return DAO.update(id, ns.payload), 204

    @ns.doc('delete_deal')
    @ns.response(204, 'Deal deleted')
    def delete(self, id):
        """Delete a data collection"""
        DAO.delete(id)
        return '', 204
