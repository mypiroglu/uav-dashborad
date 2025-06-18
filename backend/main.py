from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import random


def drone_simulator():
    """Yield simulated telemetry data."""
    lat = 39.9200
    lon = 32.8500
    while True:
        lat += random.uniform(0.00005, 0.0002)
        lon += random.uniform(0.00005, 0.0002)
        yield {
            "lat": lat,
            "lon": lon,
            "battery": random.randint(60, 100),
            "altitude": random.randint(90, 120),
        }

app = FastAPI()

# CORS izinleri
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def status():
    return {"server": "ok"}

@app.get("/status")
def status():
    return {"status": "ok"}

@app.websocket("/ws/track")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    simulator = drone_simulator()
    while True:
        data = next(simulator)
        await websocket.send_json(data)
        await asyncio.sleep(1)
