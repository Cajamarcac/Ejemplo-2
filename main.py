from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from faker import Faker

app = FastAPI()
fake = Faker()

class User(BaseModel):
    username: str
    email: str

@app.get("/users/", response_model=List[User])
async def read_users():
    users = []
    for _ in range(10):
        user = User(username=fake.user_name(), email=fake.email())
        users.append(user)
    return users

@app.get("/", response_model=dict)
async def read_root():
    return {"message": "Bienvenid@ esta es una prueba de fast api en GitHub!"}

# Otros Endpoints:

@app.get("/user/{user_id}", response_model=User)
async def read_user(user_id: int):
    # Lógica para obtener información de un usuario específico (simulado con Faker)
    return User(username=fake.user_name(), email=fake.email())

@app.post("/user/", response_model=User)
async def create_user(user: User):
    # Lógica para crear un nuevo usuario (puede almacenarse en una base de datos, por ejemplo)
    return user

@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    # Lógica para actualizar la información de un usuario existente
    return user

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    # Lógica para eliminar un usuario
    return {"message": f"User {user_id} deleted successfully"}










# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List
# from faker import Faker

# app = FastAPI()
# fake = Faker()

# class User(BaseModel):
#     username: str
#     email: str

# @app.get("/users/", response_model=List[User])
# async def read_users():
#     users = []
#     for _ in range(10):
#         user = User(username=fake.user_name(), email=fake.email())
#         users.append(user)
#     return users

# @app.get("/", response_model=dict)
# async def read_root():
#     return {"message": "Bienvenid@ esta es una prueba de fast api en GitHub!"}























# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# from faker import Faker

# app = FastAPI()
# fake = Faker()

# class User(BaseModel):
#     username: str
#     email: str

# @app.get("/users/", response_model=List[User])
# async def read_users():
#     users = []
#     for _ in range(10):
#         user = User(username=fake.user_name(), email=fake.email())
#         users.append(user)
#     return users
