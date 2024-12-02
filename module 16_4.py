import asyncio
from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

users = []
class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/users')
async def get_all_users() -> list(users):
    return users


@app.post('/user/{username}/{age}')
async def post_user(user: User, username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='Valery')],
        age: int = Path(ge=18, le=120, description="Enter age", examples='55')):

    if users is False:
        user.id = 1
    else:
        user.id = len(users) + 1

    user.username = username
    user.age = age
    users.append(user)


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user: User, user_id: int,
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='Valery')],
                      age: int = Path(ge=18, le=120, description="Enter age", examples='55')):
    try:
        for user_id in users:
            if user_id == user.id:
                user.username = username
                user.age = age
            return f"The user {user_id} is updated."
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user: User, user_id: int):
    try:
        for index in users:
            if user_id == user.id:
                users.pop(index)
            return f"Пользователь с ID {user_id} удален."

    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
