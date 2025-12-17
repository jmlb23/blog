from fastapi import FastAPI
from features.users import routes as userRouter
from features.posts import routes as postRouter


app = FastAPI()
app.include_router(userRouter.userRouter)
app.include_router(postRouter.postRouter)
