from flask import Flask
from flask import request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import os


app = Flask(__name__)

mongodb_host = os.environ.get('MONGO_HOST', 'mongo')
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))


client = MongoClient(mongodb_host, mongodb_port)

db = client['items']

collection = db['items']


@app.route("/all")
def root():
    return dumps(collection.find())


@app.route("/sold")
def get_sold():
    return dumps(collection.find_one({'sold': "yes"}))


@app.route("/not_sold")
def get_not_sold():
    return dumps(collection.find_one({'sold': "no"}))


@app.route("/search_by_name")
def search_by_name():
    name = request.values.get("name")
    return dumps(collection.find({"name": name}))



@app.route("/mark_as_sold")
def mark_as_sold():
    item_id = request.values.get("_id")
    collection.update_one({"_id": ObjectId(item_id)}, {"$set": {"sold": "yes"}})
    return "The card has been marked as sold"


@app.route("/add", methods=['POST'])
def add():
    name = request.values.get("name")
    date = request.values.get("date")
    collection.insert_one({
        "name": name,
        "date": date,
        "sold": "no"
    })
    return "A new item has been added"


@app.route("/delete")
def remove():
    key = request.values.get("_id")
    collection.delete_one({"_id": ObjectId(key)})
    return "The card has been successfully deleted"










