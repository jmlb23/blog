from pydantic import BaseModel
from datetime import date


class Post(BaseModel):
    description: str
    created: date
