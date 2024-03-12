# Endpoint 1: /
curl http://localhost:8000/

# Endpoint 2: /users/
curl http://localhost:8000/users/

# Endpoint 3: /user/{user_id}
curl http://localhost:8000/user/1

# Endpoint 4: /user/ (POST request)
curl -X POST -H "Content-Type: application/json" -d '{"username": "john_doe", "email": "john.doe@example.com"}' http://localhost:8000/user/

# Endpoint 5: /user/{user_id} (PUT request)
curl -X PUT -H "Content-Type: application/json" -d '{"username": "updated_username", "email": "updated.email@example.com"}' http://localhost:8000/user/1

# Endpoint 6: /user/{user_id} (DELETE request)
curl -X DELETE http://localhost:8000/user/1
