from fastapi import APIRouter, Depends
from .dto import Comment, CreateComment
from ..auth import helpers
from .model import get_repo, AbstractCommentRepository
from typing import Annotated, Any


commentsRouter = APIRouter()


@commentsRouter.get("/comments/{post_id}/comments")
def get_comments_by_post(
    token: Annotated[dict[str, Any], Depends(helpers.get_current_user)],
    repo: Annotated[AbstractCommentRepository, Depends(get_repo)],
    post_id: str
) -> list[Comment]:
    comments_by_post = repo.get_by_postid(post_id)
    return comments_by_post


@commentsRouter.post("/comments/{post_id}/comments")
def add_comment_to_post(
    token: Annotated[dict[str, Any], Depends(helpers.get_current_user)],
    repo: Annotated[AbstractCommentRepository, Depends(get_repo)],
    post_id: str,
    comment: CreateComment
) -> str | None:
    return repo.add(Comment(
        post_id=comment.post_id,
        content=comment.content
    ))
