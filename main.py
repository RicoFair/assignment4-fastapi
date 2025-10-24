from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

class User(BaseModel):
    name: str
    age: int
    is_student: bool = False

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_id": user_id, **user.dict()}
