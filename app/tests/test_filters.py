import socket
import json
import pytest

HOST = 'localhost'
PORT = 5050

def send_request(filters):
    with socket.create_connection((HOST, PORT)) as s:
        s.sendall(json.dumps(filters).encode("utf-8"))
        data = s.recv(8192)
        return json.loads(data.decode("utf-8"))

def test_filter_by_brand():
    filters = {"brand": "Ford"}
    response = send_request(filters)
    
    assert isinstance(response, list)
    if response:
        for car in response:
            assert car["brand"] == "Ford", f"Expected brand 'Ford', got '{car['brand']}'"

def test_filter_ford_fiesta():
    filters = {"brand": "Ford", "model": "Fiesta"}
    response = send_request(filters)

    assert isinstance(response, list)
    assert len(response) > 0, "No cars found for brand 'Ford' and model 'Fiesta'"

    for car in response:
        assert car["brand"] == "Ford", f"Expected brand 'Ford', got '{car['brand']}'"
        assert car["model"] == "Fiesta", f"Expected model 'Fiesta', got '{car['model']}'"
