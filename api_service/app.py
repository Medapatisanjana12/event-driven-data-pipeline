from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")
db = client.sensor_db
collection = db.events

@app.route("/data")
def get_data():

    data = list(collection.find({},{"_id":0}))

    return jsonify(data)

@app.route("/health")
def health():
    return {"status":"healthy"}

app.run(host="0.0.0.0",port=8000)
