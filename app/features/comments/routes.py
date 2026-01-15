from fastapi import APIRouter, Depends
from .dto import Comment
from ..auth import helpers
from .model import get_repo
from typing import Annotated, Any


commentsRouter = APIRouter()


@commentsRouter.get("/comments/{post_id}/comments")
def get_comments_by_post(
    token: Annotated[dict[str, Any], Depends(helpers.get_current_user)],
    repo: Annotated[Any, Depends(get_repo)],
    post_id: str
) -> list[Comment]:
    pass
