import bson.json_util as json

from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
from flask_pymongo import MongoClient

client = MongoClient('mongodb://cbeasley92:1sL#ak23@cluster0-shard-00-00-klqia.mongodb.net:27017,'
                     'cluster0-shard-00-01-klqia.mongodb.net:27017,'
                     'cluster0-shard-00-02-klqia.mongodb.net:27017/wfd'
                     '?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')


class Foods(Resource):
    def __init__(self):
        self.db = client.wfd

    def get(self):
        return json.dumps(self.db.food.find()[0])


class Food(Resource):
    def __init__(self):
        self.db = client.wfd

    def get(self, upc):
        if len(upc) == 14:
            resp = json.dumps(self.db.food.find({'upc14': upc})[0])
        elif len(upc) == 12:
            resp = json.dumps(self.db.food.find({'upc12': upc})[0])
        else:
            resp = json.dumps({})

        print resp
        return resp

    def post(self, upc):
        data = request.get_json(force=True)
        self.db.food.replace_one({'upc14': upc}, data, upsert=True)
        print 'Data: %s' % data
        return json.dumps({"results": list(self.db.food.find(data))})

    def put(self, upc):  # Testing
        data = request.get_json(force=True)
        print 'Data: %s' % data
        self.db.food.update({'upc14': upc}, data)


class Brand(Resource):
    def __init__(self):
        self.db = client.wfd

    def get(self, brand_name):
        resp = json.dumps(self.db.food.find({'brand': brand_name})[0])
        print resp
        return resp

    def post(self, brand_name):
        data = request.get_json(force=True)
        self.db.food.replace_one({'brand': brand_name}, data, upsert=True)
        print 'Data: %s' % data
        return json.dumps({"results": list(self.db.food.find(data))})

    def put(self, brand_name):  # Testing
        data = request.get_json(force=True)
        print 'Data: %s' % data
        self.db.food.update({'brand': brand_name}, data)
        

class Name(Resource):
    def __init__(self):
        self.db = client.wfd

    def get(self, food_name):
        resp = json.dumps(self.db.food.find({'name': food_name})[0])
        print resp
        return resp

    def post(self, food_name):
        data = request.get_json(force=True)
        self.db.food.replace_one({'name': food_name}, data, upsert=True)
        print 'Data: %s' % data
        return json.dumps({"results": list(self.db.food.find(data))})

    def put(self, food_name):  # Testing
        data = request.get_json(force=True)
        print 'Data: %s' % data
        self.db.food.update({'name': food_name}, data)
