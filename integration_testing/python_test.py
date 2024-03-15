import requests

# URL base de la aplicación FastAPI
base_url = "http://localhost:8000"  # Ajusta la URL según la configuración de tu aplicación

def test_read_root():
    response = requests.get(base_url + "/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenid@ esta es una prueba de fast api en GitHub!"}

def test_read_users():
    response = requests.get(base_url + "/users/")
    assert response.status_code == 200
    assert len(response.json()) == 10  # Verifica que se devuelvan 10 usuarios simulados

def test_read_user():
    response = requests.get(base_url + "/user/1")
    assert response.status_code == 200
    # Puedes agregar más aserciones según la respuesta esperada

def test_create_user():
    user_data = {"username": "john_doe", "email": "john.doe@example.com"}
    response = requests.post(base_url + "/user/", json=user_data)
    assert response.status_code == 200
    # Puedes agregar más aserciones según la respuesta esperada

def test_update_user():
    user_data = {"username": "updated_username", "email": "updated.email@example.com"}
    response = requests.put(base_url + "/user/1", json=user_data)
    assert response.status_code == 200
    # Puedes agregar más aserciones según la respuesta esperada

def test_delete_user():
    response = requests.delete(base_url + "/user/1")
    assert response.status_code == 200
    # Puedes agregar más aserciones según la respuesta esperada

if __name__ == "__main__":
    # Ejecuta todas las funciones de prueba si el script se ejecuta directamente
    test_read_root()
    test_read_users()
    test_read_user()
    test_create_user()
    test_update_user()
    test_delete_user()