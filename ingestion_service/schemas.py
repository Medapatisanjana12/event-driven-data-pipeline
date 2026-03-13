from pydantic import BaseModel
from datetime import datetime

class Location(BaseModel):
    latitude: float
    longitude: float

class SensorData(BaseModel):
    sensor_id: str
    timestamp: datetime
    temperature: float
    humidity: float
    location: Location
