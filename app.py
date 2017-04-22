import bson.json_util as json

from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
from flask_pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://cbeasley92:1sL#ak23@cluster0-shard-00-00-klqia.mongodb.net:27017,'
                     'cluster0-shard-00-01-klqia.mongodb.net:27017,'
                     'cluster0-shard-00-02-klqia.mongodb.net:27017/wfd'
                     '?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')


class Root(Resource):
    def get(self):
        return 'Welcome to What\'s for Dinner API'


class Users(Resource):
    def __init__(self):
        self.db = client.wfd

    def get(self):
        count = self.db.users.count()
        print 'Number of users found: %s' % count

        if count > 0:
            user_list = list(self.db.users.find())
            for user in user_list:
                print user

            return json.dumps({"results": user_list})
        else:
            return json.dumps({})


class User(Resource):
    def __init__(self):
        self.db = client.wfd

    def get(self, username):
        resp = json.dumps(self.db.users.find({'username': username})[0])
        print resp
        return resp

    def post(self, username):
        data = request.get_json(force=True)
        self.db.users.replace_one({'username': username}, data, upsert=True)
        print 'Data: %s' % data
        return json.dumps({"results": list(self.db.users.find(data))})

    def put(self, username):  # Testing
        data = request.get_json(force=True)
        print 'Data: %s' % data
        self.db.users.update({'username': username}, data)

api.add_resource(Root, '/')
api.add_resource(Users, '/api/users')
api.add_resource(User, '/api/user/<username>')

if __name__ == '__main__':
    app.run(debug=True)
