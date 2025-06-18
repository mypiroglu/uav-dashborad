from concurrent.futures import process
import time
import random
import json
from websocket import create_connection

# WebSocket'e bağlan
ws = create_connection("ws://localhost:8000/ws/track")  # Eğer port değiştirdiysen burayı güncelle

# Başlangıç konumu
lat = 39.9200
lon = 32.8500

while True:
    lat += random.uniform(0.00005, 0.0002)
    lon += random.uniform(0.00005, 0.0002)

    data = {
        "lat": lat,
        "lon": lon,
        "battery": random.randint(60, 100),
        "altitude": random.randint(90, 120),
    }

    ws.send(json.dumps(data))
    print(f"Sent: {data}")
    time.sleep(1)
