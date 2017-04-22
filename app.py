from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
from Food import Food

from Users import User, Users

app = Flask(__name__)
api = Api(app)


class Root(Resource):
    def get(self):
        return 'Welcome to What\'s for Dinner API'


api.add_resource(Root, '/')
api.add_resource(Users, '/api/users')
api.add_resource(User, '/api/user/<username>')
api.add_resource(Food, '/api/food/<upccode>')

if __name__ == '__main__':
    app.run(debug=True)
