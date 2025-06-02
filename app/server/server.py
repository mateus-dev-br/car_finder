import socket
import json
from app.db.database import SessionLocal
from app.models.car import Car

HOST = 'localhost'
PORT = 5050

def handle_request(data: dict):
    session = SessionLocal()
    query = session.query(Car)

    # Apply filters
    if 'brand' in data:
        query = query.filter(Car.brand.ilike(f"{data['brand']}"))
    if 'model' in data:
        query = query.filter(Car.model.ilike(data['model']))
    if 'year' in data:
        try:
            query = query.filter(Car.year == int(data['year']))
        except ValueError:
            pass
    if 'fuel_type' in data:
        query = query.filter(Car.fuel_type.ilike(f"{data['fuel_type']}"))

    results = query.limit(10).all()
    session.close()

    return [
        {
            "brand": car.brand,
            "model": car.model,
            "year": car.year,
            "color": car.color,
            "mileage": car.mileage,
            "price": car.price,
            "transmission": car.transmission,
            "fuel_type": car.fuel_type
        }
        for car in results
    ]

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"🚀 MCP Server running on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(4096)
                if not data:
                    continue

                try:
                    filters = json.loads(data.decode('utf-8'))
                    print(f"Filters received: {filters}")
                    response = handle_request(filters)
                    print(f"ending {len(response)} result(s)")
                    conn.sendall(json.dumps(response).encode('utf-8'))
                except Exception as e:
                    error = {"error": "Internal server error", "details": str(e)}
                    conn.sendall(json.dumps(error).encode('utf-8'))

if __name__ == "__main__":
    start_server()
