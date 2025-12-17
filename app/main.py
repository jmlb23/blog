from fastapi import FastAPI
from features.users import routes as userRoutes
from features.posts import routes as postRoutes


app = FastAPI(description="a blog api", title="blog")

app.include_router(userRoutes.userRouter)
app.include_router(postRoutes.postRouter)
