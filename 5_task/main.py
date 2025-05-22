from typing import Annotated
from fastapi import FastAPI, Depends, Query, HTTPException, status

app = FastAPI()

# ---------- SIMPLE DEPENDENCY ----------
def get_simple_goal() -> dict:
    return {"goal": "Here is my goal: building AI Agents"}

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}


@app.get("/goal")
def read_goal(goal: Annotated[dict, Depends(get_simple_goal)]):
    return goal

# ---------- USERNAME DEPENDENCY ----------
def extract_username(username: str = Query(..., description="Username")) -> dict:
    return {"username": username}

@app.get("/user")
def read_user(user: Annotated[dict, Depends(extract_username)]):
    return user

# ---------- LOGIN CHECK DEPENDENCY ----------
def verify_login(
    phone_number: str = Query(None, description="Phone number"),
    password: str = Query(None, description="Password")
) -> dict:
    if phone_number and password == "1234":
        return {"message": "Login successful"}
    return {"message": "Login failed"}

@app.get("/login")
def login_check(response: Annotated[dict, Depends(verify_login)]):
    return response

# ---------- MULTIPLE DEPENDENCIES ----------
def increment_by_one(num: int) -> int:
    return num + 1

def increment_by_two(num: int) -> int:
    return num + 2

@app.get("/calculate/{num}")
def calculate_total(
    num: int,
    add_one: Annotated[int, Depends(increment_by_one)],
    add_two: Annotated[int, Depends(increment_by_two)]
):
    total = num + add_one + add_two
    return {"total": total}

# ---------- CUSTOM CLASS DEPENDENCY ----------
blogs_data = {
    "1": "GenAI",
    "2": "FastAPI",
    "3": "Pydantic"
}

users_data = {
    "6": "sajeel",
    "7": "kahn"
}

class ObjectFetcher:
    def __init__(self, source: dict):
        self.source = source

    def __call__(self, id: str):
        obj = self.source.get(id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Object with ID '{id}' not found"
            )
        return obj

fetch_blog = ObjectFetcher(blogs_data)
fetch_user = ObjectFetcher(users_data)

@app.get("/blogs/{id}")
def get_blog(blog: Annotated[str, Depends(fetch_blog)]):
    return {"blog": blog}

@app.get("/users/{id}")
def get_user(user: Annotated[str, Depends(fetch_user)]):
    return {"user": user}