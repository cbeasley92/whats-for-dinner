import bson.json_util as json

from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
from flask_pymongo import MongoClient

client = MongoClient('mongodb://cbeasley92:1sL#ak23@cluster0-shard-00-00-klqia.mongodb.net:27017,'
                     'cluster0-shard-00-01-klqia.mongodb.net:27017,'
                     'cluster0-shard-00-02-klqia.mongodb.net:27017/wfd'
                     '?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')


class House(Resource):
    def __init__(self):
        self.db = client.wfd

    def get(self, house_name):
        resp = json.dumps(self.db.users.find({'house': house_name})[0])
        print resp
        return resp

    def post(self, house_name):
        data = request.get_json(force=True)
        if type(data) == str:
            data = json.loads(data)
        self.db.users.replace_one({'house': house_name}, data, upsert=True)
        print 'Data: %s' % data
        return json.dumps({"results": list(self.db.users.find(data))})

    def put(self, house_name):  # Testing
        data = request.get_json(force=True)
        print 'Data: %s' % data
        self.db.users.update({'house': house_name}, data)
        

class HouseFood(Resource):
    def __init__(self):
        self.db = client.wfd

    def get(self, house_name):
        house_resp = self.db.users.find({'house': house_name})[0]
        resp = json.dumps(house_resp['food'])
        return resp

    def post(self, house_name):
        data = request.get_json(force=True)
        if type(data) == str:
            data = json.loads(data)
        self.db.users.update({'house': house_name}, data, upsert=True)
        print 'Data: %s' % data
        return json.dumps({"results": list(self.db.users.find(data))})

    def put(self, house_name):  # Testing
        data = request.get_json(force=True)
        print 'Data: %s' % data
        self.db.users.update({'house': house_name}, data, upsert=True)
