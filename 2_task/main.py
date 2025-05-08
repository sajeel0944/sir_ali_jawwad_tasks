from fastapi import FastAPI

app = FastAPI()
user_name : str = None

@app.post("/create")
def create(name: str) -> dict:
    global user_name
    user_name = name
    return {"user" : f"My name is {user_name}"}


@app.get("/read")
def read() -> dict:
    global user_name
    if user_name:
        return {"user": f"wellcome to {user_name}" }
    else:
        return {"user" : "invaild"}
    

@app.put("/update")
def update(name : str) -> dict:
    global user_name
    user_name = name
    if user_name:
        return {"user" : f"My name is {user_name}"}
    else:
        return {"user" : "invaild"}
    

@app.delete("/dalete")
def delete() -> dict:
    global user_name
    user_name  = None
    return {"user" : f"My name is {user_name}"}

