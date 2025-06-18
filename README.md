# UAV Dashboard

This project provides a simple drone tracking demo. The backend uses FastAPI to broadcast simulated telemetry over a WebSocket endpoint, and the frontend shows the location on a map.

## Running the demo

1. Install the backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the API server:
   ```bash
   uvicorn backend.main:app --reload --port 8000
   ```
3. Install frontend packages and start the dev server:
   ```bash
   cd frontend
   npm install --legacy-peer-deps
   npm run dev
   ```

Open `http://localhost:3000` in a browser to see the map update in real time.
