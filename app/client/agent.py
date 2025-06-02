import socket
import json
from app.db.constants import brands_models, fuel_types

HOST = 'localhost'
PORT = 5050

def get_user_filters() -> dict:
    """Collect user filters in a guided, step-by-step interaction."""
    print("🚗 Hello! Let's find your ideal car.\n")

    # Step 1: Choose brand
    brands = list(brands_models.keys())
    print("Which brand are you looking for?")
    print(f"Available options: {', '.join(brands)}")
    
    brand = ""
    while brand not in brands:
        brand = input("Type a brand: ").strip().capitalize()
        if brand not in brands:
            print("⚠️  Brand not recognized. Please choose from the available options.")

    # Step 2: Choose model from that brand
    available_models = brands_models[brand]
    print(f"\nModels available for {brand}: {', '.join(available_models)}")

    model = ""
    while model not in available_models:
        model = input("Type a model: ").strip().capitalize()
        if model not in available_models:
            print("⚠️  Model not recognized. Please choose from the available options.")

    # Step 3: Choose fuel type
    print(f"\nWhat is your preferred fuel type?")
    print(f"Available options: {', '.join(fuel_types)}")

    fuel = None
    while True:
        fuel_input = input("Type a fuel type (or press Enter to skip): ").strip().capitalize()
        if not fuel_input:
            fuel = None
            break
        if fuel_input in fuel_types:
            fuel = fuel_input
            break
        else:
            print("⚠️  Fuel type not recognized. Please choose from the available options.")


    # Build filter dict
    filters = {
        "brand": brand,
        "model": model
    }
    if fuel:
        filters["fuel_type"] = fuel

    return filters


def send_request(filters: dict) -> list:
    """Send the user-defined filters to the server and return the results."""
    try:
        with socket.create_connection((HOST, PORT), timeout=5) as s:
            s.sendall(json.dumps(filters).encode('utf-8'))
            data = s.recv(8192)
            return json.loads(data.decode('utf-8'))
    except (ConnectionRefusedError, socket.timeout) as e:
        print("❌ Failed to connect to the server. Is it running?")
        return []


def show_results(results):
    print("\n🔍 Matching results:\n")
    if not results:
        print("No cars found with the provided filters.")
        return

    for i, car in enumerate(results, start=1):
        print(f"{i}. {car['brand']} {car['model']} ({car['year']})")
        print(f"   Color: {car['color']}")
        print(f"   Mileage: {car['mileage']} km")
        print(f"   Transmission: {car['transmission']} | Fuel: {car['fuel_type']}")
        print(f"   Price: R$ {car['price']:,.2f}")
        print("-" * 40)

def main():
    filters = get_user_filters()
    response = send_request(filters)
    show_results(response)

if __name__ == "__main__":
    main()
