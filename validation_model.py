from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    '''
    This is a pydantic model for the post class which checks whether the name is a string, age is an integer, published is a boolean and rating is optional. 
    '''
    name: str
    age: int
    published: bool = True
    rating: Optional[int] = None

