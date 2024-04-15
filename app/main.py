from fastapi import FastAPI

app = FastAPI()   

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]



