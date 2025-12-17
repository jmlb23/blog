from fastapi import APIRouter


userRouter = APIRouter()


@userRouter.get("/user")
def user() -> dict[str, str]:
    return {"hello": "world"}
