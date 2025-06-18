'use client'
import { useState, useEffect } from 'react';
import { ComposableMap, Geographies, Geography, Marker } from 'react-simple-maps';

const geoUrl = '/world.geo.json';

export default function Home() {
  const [position, setPosition] = useState<[number, number]>([32.85, 39.92]);

  useEffect(() => {
    const url = process.env.NEXT_PUBLIC_WS_URL || 'ws://localhost:8000/ws/track';
    const ws = new WebSocket(url);
    ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        setPosition([data.lon, data.lat]);
      } catch (err) {
        console.error('invalid data', err);
      }
    };
    return () => ws.close();
  }, []);

  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <ComposableMap projectionConfig={{ scale: 150 }} style={{ width: '100%', height: '100%' }}>
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map(geo => (
              <Geography key={geo.rsmKey} geography={geo} fill="#EAEAEC" stroke="#D6D6DA" />
            ))
          }
        </Geographies>
        <Marker coordinates={position}>
          <circle r={4} fill="#F00" />
        </Marker>
      </ComposableMap>
    </div>
  );
}
