from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api

from Users import User, Users
from Food import Foods, Food, Name, Brand

app = Flask(__name__)
api = Api(app)


class Root(Resource):
    def get(self):
        return 'Welcome to What\'s for Dinner API'


api.add_resource(Root, '/')
api.add_resource(Users, '/api/users')
api.add_resource(User, '/api/user/<username>')
api.add_resource(Foods, '/api/food')
api.add_resource(Food, '/api/food/upc/<upc>')
api.add_resource(Name, '/api/food/name/<item_name>')
api.add_resource(Brand, '/api/food/brand/<brand_name>')


if __name__ == '__main__':
    app.run(debug=True)
