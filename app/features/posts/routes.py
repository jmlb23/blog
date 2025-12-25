from fastapi import APIRouter, Depends
from typing import Annotated
from .model import AbstractPostRepository, Post, get_repo
from .dto import PostCreatedResponse, Post as PostDTO

postRouter = APIRouter()


@postRouter.get("/posts")
def get_posts(
    repo: Annotated[AbstractPostRepository, Depends(get_repo)]
) -> list[Post]:
    return repo.list()


@postRouter.get("/posts/{post_id}")
def get_post_by_id(
    post_id: str,
    repo: Annotated[AbstractPostRepository, Depends(get_repo)]
) -> Post | None:
    return repo.get(post_id)


@postRouter.post("/posts")
def add_post(
    post: PostDTO,
    repo: Annotated[AbstractPostRepository, Depends(get_repo)]
) -> PostCreatedResponse | None:
    id = repo.add(Post(post.description, post.created))
    if id is not None:
        return PostCreatedResponse(id=id)
    else:
        return None
