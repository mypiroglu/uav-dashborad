from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import random

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

    # Başlangıç koordinatları
    lat = 39.9200
    lon = 32.8500

    while True:
        # Her seferinde küçük bir hareket
        lat += random.uniform(0.00005, 0.0002)
        lon += random.uniform(0.00005, 0.0002)

        # Telemetri verisi
        data = {
            "lat": lat,
            "lon": lon,
            "battery": random.randint(70, 100),
            "altitude": random.randint(95, 115)
        }

        await websocket.send_json(data)
        await asyncio.sleep(1)
