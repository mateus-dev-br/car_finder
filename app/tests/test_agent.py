import socket
import json

HOST = 'localhost'
PORT = 5050

def test_agent_connection_and_response():
    filtros = {
        "brand": "Toyota",
        "fuel_type": "Gasoline"
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(filtros).encode('utf-8'))

        data = s.recv(8192)
        resposta = json.loads(data.decode('utf-8'))

        assert isinstance(resposta, list)
        if resposta:
            car = resposta[0]
            assert "brand" in car
            assert "model" in car
            assert "price" in car
