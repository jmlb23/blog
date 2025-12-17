from fastapi import FastAPI
from features.users import routes as userRoutes
from features.posts import routes as postRoutes


app = FastAPI()

app.include_router(userRoutes.userRouter)
app.include_router(postRoutes.postRouter)
