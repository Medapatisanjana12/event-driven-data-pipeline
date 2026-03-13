from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
from schemas import SensorData

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route("/ingest", methods=["POST"])
def ingest():

    try:
        data = request.json
        validated = SensorData(**data)

        producer.send("sensor_events", validated.dict())

        return jsonify({"status":"success"}),200

    except Exception as e:
        return jsonify({"error":str(e)}),400


@app.route("/health")
def health():
    return {"status":"healthy"}
    

app.run(host="0.0.0.0",port=5000)
