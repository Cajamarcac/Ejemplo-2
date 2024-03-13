from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenid@ esta es una prueba de fast api en GitHub!"}

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 10


