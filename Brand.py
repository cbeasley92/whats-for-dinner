import bson.json_util as json

from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
from flask_pymongo import MongoClient

client = MongoClient('mongodb://cbeasley92:1sL#ak23@cluster0-shard-00-00-klqia.mongodb.net:27017,'
                     'cluster0-shard-00-01-klqia.mongodb.net:27017,'
                     'cluster0-shard-00-02-klqia.mongodb.net:27017/wfd'
                     '?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')


class Brand(Resource):
    def __init__(self):
        self.db = client.wfd

    def get(self, brandname):
        resp = json.dumps(self.db.food.find({'brand': brandname})[0])
        print resp
        return resp

    def post(self, brandname):
        data = request.get_json(force=True)
        self.db.food.replace_one({'brand': brandname}, data, upsert=True)
        print 'Data: %s' % data
        return json.dumps({"results": list(self.db.food.find(data))})

    def put(self, brandname):  # Testing
        data = request.get_json(force=True)
        print 'Data: %s' % data
        self.db.food.update({'brand': brandname}, data)