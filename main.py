from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/post")
async def post(payload:dict=Body(...)):
    return {"message": f"Hello World {payload['name']}" }