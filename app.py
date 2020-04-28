from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'Umar'
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
            data = request.get_json()
            item = {'name': name, 'price': data['price']}
            items.append(item)
            return item, 201

class Itemlist(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item,  '/item/<string:name>')
api.add_resource(Itemlist,  '/items')

app.run(port=5000, debug=True)
