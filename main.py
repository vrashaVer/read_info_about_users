from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List


app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
# users: List[User] = []

users = [
    User(id=1, username="user1", email="user1@gmail.com"),
    User(id=2, username="user2", email="user2@gmail.com")
]

current_id = 2

@app.post("/users/{user_id}", response_model=User)
def get_user_by_id(id:int):
    for user in users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="Користувач не знайден")


@app.post("/users", response_model=List[User])
def get_users():
    return users


@app.post("/create_user", response_model=CreateUserRequest)
def add_user(user : CreateUserRequest):
    
    global current_id
    current_id += 1
    new_user = User(id=current_id, username=user.username, email=user.email)
    users.append(new_user)
    return new_user








  

