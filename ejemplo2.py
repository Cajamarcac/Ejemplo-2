from fastapi import FastAPI
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
