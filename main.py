from fastapi import FastAPI
from fastapi.params import Body
from validation_model import Post


app = FastAPI()

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
async def post(post:Post):
    return post.model_dump()

    
