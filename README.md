# Event-Driven Data Pipeline

## Overview

This project implements a **real-time event-driven data pipeline** using **Kafka, MongoDB, Docker, and Python microservices**.
Sensor data is generated, sent to Kafka through an ingestion service, stored in MongoDB by a consumer service, and retrieved through an API.

## Architecture

Generator → Ingestion Service → Kafka → Consumer → MongoDB → API Service

## Technologies

* Python
* Apache Kafka
* MongoDB
* Docker & Docker Compose
* Flask / FastAPI

## Project Structure

```
generator/
ingestion_service/
consumer_service/
api_service/
tests/
docker-compose.yml
README.md
```

## Run the Project

Start all services:

```
docker compose up --build
```

## API Endpoint

Get stored sensor data:

```
GET http://localhost:8000/data
```

## Author

Sanjana Medapati
