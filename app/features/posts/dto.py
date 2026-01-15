from pydantic import BaseModel
from datetime import date


class PostCreatedResponse(BaseModel):
    id: str


class Post(BaseModel):
    description: str
    created: date
