from fastapi import APIRouter


userRouter = APIRouter()


@userRouter.get("/users")
def user() -> dict[str, str]:
    return {"hello": "world"}
