from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    '''
    This is a pydantic model for the post class which checks whether the title is a string, content is a string, published is a boolean ,rating is optional and id is an integer. We are using the pydantic library to validate the data and don't allow extra fields
    '''
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    id: Optional[int] = None

    class Config:
        extra = "forbid"
