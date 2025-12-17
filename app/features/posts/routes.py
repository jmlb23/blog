from fastapi import APIRouter


postRouter = APIRouter()


@postRouter.get("/posts")
def get_posts() -> dict[str, str]:
    return {"One": "Post"}
