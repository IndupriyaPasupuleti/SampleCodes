from fastapi import FastAPI, HTTPException
from schemas import User
from models import users_db

app = FastAPI()

@app.post("/users", response_model=User)
def add_user(user: User):
    # Check if user already exists
    for existing_user in users_db:
        if existing_user['id'] == user.id:
            raise HTTPException(status_code=400, detail="User with this ID already exists")
    users_db.append(user.dict())
    return user

@app.get("/users", response_model=list[User])
def get_users():
    return users_db
