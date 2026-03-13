from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer(
    'sensor_events',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

client = MongoClient("mongodb://mongodb:27017/")
db = client.sensor_db
collection = db.events

for msg in consumer:
    data = msg.value

    unique_id = f"{data['sensor_id']}_{data['timestamp']}"

    try:
        collection.insert_one(data)
        print("Saved:",unique_id)
    except:
        print("Duplicate or error")
