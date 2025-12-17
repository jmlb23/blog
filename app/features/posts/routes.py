from fastapi import APIRouter, Depends
from typing import Annotated
from .model import PostRepository, Post


postRouter = APIRouter()


@postRouter.get("/posts")
def get_posts(
    repo: Annotated[PostRepository, Depends()]
) -> list[Post]:
    return repo.list()


@postRouter.get("/posts/{post_id}")
def get_post_by_id(
        post_id: str,
        repo: Annotated[PostRepository, Depends()]
) -> Post | None:
    return repo.get(post_id)
