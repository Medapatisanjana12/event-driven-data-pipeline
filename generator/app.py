import requests
import time
import random
from datetime import datetime

URL = "http://ingestion_service:5000/ingest"

def generate_sensor_data():
    return {
        "sensor_id": f"sensor_{random.randint(1,5)}",
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": random.uniform(20,30),
        "humidity": random.uniform(40,70),
        "location":{
            "latitude": 34.05,
            "longitude": -118.24
        }
    }

while True:
    data = generate_sensor_data()
    try:
        requests.post(URL,json=data)
        print("Sent:",data)
    except:
        print("Failed to send")

    time.sleep(3)
