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
    return {"message": "Bienvenid@ esta es una prueba de FastAPI en GitHub!"}

@app.get("/user/{user_id}", response_model=User)
async def read_user(user_id: int):
    if user_id < 1 or user_id > 10:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return User(username=fake.user_name(), email=fake.email())

@app.post("/user/", response_model=User)
async def create_user(user: User):
    return user

@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    if user_id < 1 or user_id > 10:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@app.delete("/user/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    if user_id < 1 or user_id > 10:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": f"Usuario {user_id} eliminado exitosamente"}
