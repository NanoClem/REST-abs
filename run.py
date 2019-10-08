import markdown
from flask import Flask
from flask_restplus import Resource, Api, fields


# Instance of Flask
app = Flask(__name__)
api = Api(app)



#=============================================================
#   MODEL
#=============================================================
deal = api.model('Deal', {
    "id"  : fields.Integer(readonly=True, description="The deal unique identifier"),
    "url" : fields.String(required=True, description="The deal url")
    })

class DealModel(object):
    """
    """
    def __init__(self):
        """ """
        self.deals = []
        self.cpt   = 0

    def get(self, id):
        """Return data from a deal"""
        for deal in self.deals:
            if deal['id'] == id:
                return deal
        api.abort(404, "Deal {} doesn't exist".format(id))

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


DAO = DealModel()
DAO.create({"url" : "https://www.dealabs.com/bons-plans/tv-led-4k-uhd-55-pouces-continental-edison-smart-tv-1714763"})


#=============================================================
#   ROUTING
#=============================================================

#---------------------------------------------
#   INDEX
#---------------------------------------------
@api.route("/api")
class Index(Resource):
    def get(self):
        """Showing the API doc file"""
        with open("README.md", "r") as doc_file :
            content = doc_file.read()
            return markdown.markdown(content)

#---------------------------------------------
#   DATA LIST
#---------------------------------------------
@api.route("/api/deals")
class DataList(Resource):
    """
    Getting a list of all stored data
    """
    @api.marshal_list_with(deal)
    def get(self):
        """Return a list of deals"""
        return DAO.deals, 200

    @api.expect(deal)
    @api.marshal_with(deal, code=201)
    def post(self):
        """Create a new deal"""
        return DAO.create(api.payload), 201

#---------------------------------------------
#   CRUD
#---------------------------------------------
@api.route("/api/deal/<int:id>")
class Data(Resource):
    """
    """
    @api.marshal_with(deal)
    def get(self, id):
        """Return data about a deal"""
        return DAO.get(id), 200

    @api.marshal_with(deal)
    def put(self, id):
        """Update a data collection"""
        return DAO.update(id, api.payload), 204

    def delete(self, id):
        """Delete a data collection"""
        DAO.delete(id)
        return '', 204



if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3000", debug=True)
