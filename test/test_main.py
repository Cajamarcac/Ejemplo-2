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

def test_read_user():
    response = client.get("/user/1")
    assert response.status_code == 200

def test_create_user():
    new_user_data = {"username": "test_user", "email": "test@example.com"}
    response = client.post("/user/", json=new_user_data)
    assert response.status_code == 200

def test_update_user():
    updated_user_data = {"username": "updated_username", "email": "updated.email@example.com"}
    response = client.put("/user/1", json=updated_user_data)
    assert response.status_code == 200

def test_delete_user():
    response = client.delete("/user/1")
    assert response.status_code == 200