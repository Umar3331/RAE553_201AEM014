from flask import Flask, request    #We get Flask class from flask module
from flask_restful import Resource, Api, abort, reqparse #Resource, Api, abort, reqparse is extracted from flask_restful to get rest api
from flask_jwt import JWT, jwt_required, identity #import JWT, jwt_required, identity from flask_jwt
from security import authenticate, identity #authenticate and identity is imported from security
from user import UserRegister #importing UserRegister
from item import Item, ItemList #Impoprting Itemlist from item


app = Flask(__name__) #Flask application is created
app.secret_key = 'Umar' #Secret line is added
api = Api(app) #this command id to create Api application instance

jwt = JWT(app, authenticate, identity) #JWT object is created and after that Flask_JWT registers has an endpoint

api.add_resource(Item,  '/item/<string:name>')
api.add_resource(ItemList,  '/items')
api.add_resource(UserRegister, 'register') # when post request is executed, UserRegister will be called and it will call post method in user.py

app.run(port=5000, debug=True)
