from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# code of get decorator


@app.get("/")
async def root():
    try:
        message = "Hello World"
        if message is None:
            raise ValueError("Message is None")
        return {"message": message}
    except Exception as e:
        return {"error": str(e)}

@app.post("/post")
async def post(payload:dict=Body(...)):
    try:
        if payload is None:
            raise ValueError("Payload is None")
        if 'name' not in payload:
            raise ValueError("Payload does not contain 'name'")
        return {"message": f"Hello World {payload['name']}"} 
    except Exception as e:
        return {"error": str(e)}
