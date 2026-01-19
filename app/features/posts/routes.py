from fastapi import APIRouter, Depends
from typing import Annotated, Any
from .model import AbstractPostRepository, Post, get_repo
from .dto import PostCreatedResponse, Post as PostDTO
from ..auth import helpers

postRouter = APIRouter()


@postRouter.get("/posts")
def get_posts(
    token: Annotated[dict[str, Any], Depends(helpers.get_current_user)],
    repo: Annotated[AbstractPostRepository, Depends(get_repo)]
) -> list[Post]:
    return repo.list()


@postRouter.get("/posts/{post_id}")
def get_post_by_id(
    token: Annotated[dict[str, Any], Depends(helpers.get_current_user)],
    post_id: str,
    repo: Annotated[AbstractPostRepository, Depends(get_repo)]
) -> Post | None:
    return repo.get(post_id)


@postRouter.post("/posts")
def add_post(
    token: Annotated[dict[str, Any], Depends(helpers.get_current_user)],
    post: PostDTO,
    repo: Annotated[AbstractPostRepository, Depends(get_repo)]
) -> PostCreatedResponse | None:
    id = repo.add(Post(post.description, post.created))
    if id is not None:
        return PostCreatedResponse(id=id)
    else:
        return None


@postRouter.delete("/posts/{post_id}")
def remove_post(
    token: Annotated[dict[str, Any], Depends(helpers.get_current_user)],
    repo: Annotated[AbstractPostRepository, Depends(get_repo)],
    post_id: str
) -> None:
    return repo.remove(post_id)
