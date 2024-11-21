from fastapi import FastAPI ,Request,Response,status,HTTPException
from fastapi.params import Body
from validation_model import Post
import sys
import random

app = FastAPI()

my_post=[{
    "title": "title one",
    "content": "content one",
    "id": 1},
    {
    "title": "title two",
    "content": "content two",
    "id": 2},
    {
    "title": "title three",
    "content": "content three",
    "id": 3}]

def fetch_post(id):
    for post in my_post:
        if post["id"]==id:
            return post
        
@app.get("/")
async def root():
    try:
        message = "Hello World"
        if message is None:
            raise ValueError("Message is None")
        return {"message": message}
    except Exception as e:
        return {"error": str(e)}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
async def post(post:Post):
    post_dict=post.model_dump()
    post_dict['id']=random.randint(1,1000)
    my_post.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
async def get_latest_post():
    post= my_post[-1]
    return {"post":post}


@app.get("/posts/{id}")
async def get_post(id:int):
    post= fetch_post(id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post":post}

@app.get("/posts")
async def get_posts():
    return {"data": my_post}


# Delete a post

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int):
    post= fetch_post(id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    my_post.remove(post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update a post

@app.put("/posts/{id}")
async def update_post(id:int,post:Post):
    post_dict=post.model_dump()
    index=-1
    for i in range(len(my_post)):
        if my_post[i]["id"]==id:
            index=i
            break
    if index==-1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    my_post[index]=post_dict
    return {"data":my_post[index]}
