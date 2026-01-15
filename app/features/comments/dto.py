from pydantic import BaseModel


class Comment(BaseModel):
    id: str
    post_id: str
    content: str
    likes: int


class CreateComment(BaseModel):
    post_id: str
    content: str
