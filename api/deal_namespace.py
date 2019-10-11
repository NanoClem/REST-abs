from flask_restplus import Namespace, Resource, fields

# api var and Metadata about the namespace
api = Namespace('api/deal', description = 'Deals related operations')



#=============================================================
#   MODEL
#=============================================================

# TEMPLATE
deal = api.model('Deal', {
    "id"  : fields.Integer(readonly=True, description="The deal unique identifier"),
    "url" : fields.String(required=True, description="The deal url")
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
        api.abort(404, "Deal {} doesn't exist".format(id), data={})

    def create(self, data):
        """Create a new data collection"""
        deal = data
        deal['id'] = self.cpt = self.cpt + 1
        self.deals.append(deal)
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
@api.route("/", strict_slashes = False)     # strict_slashes setted to False so the debuger ignores it
class DataList(Resource):
    """
    Getting a list of all stored data
    """
    @api.doc('list_deals')
    @api.marshal_list_with(deal)
    def get(self):
        """Return a list of deals"""
        return DAO.deals, 200

    @api.doc('create_deal')
    @api.expect(deal)
    @api.marshal_with(deal, code=201)
    def post(self):
        """Create a new deal"""
        return DAO.create(api.payload), 201

#---------------------------------------------
#   CRUD
#---------------------------------------------
@api.route("/<int:id>")
@api.response(404, 'Deal not found')
@api.param('id', 'The deal unique identifier')
class Data(Resource):
    """
    """
    @api.doc('get_deal')
    @api.marshal_with(deal)
    def get(self, id):
        """Return data about a deal"""
        return DAO.get(id), 200

    @api.doc('update_deal')
    @api.marshal_with(deal)
    def put(self, id):
        """Update a data collection"""
        return DAO.update(id, api.payload), 204

    @api.doc('delete_deal')
    @api.response(204, 'Deal deleted')
    def delete(self, id):
        """Delete a data collection"""
        DAO.delete(id)
        return '', 204
