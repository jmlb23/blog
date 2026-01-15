from fastapi import FastAPI
from features.users import routes as userRoutes
from features.posts import routes as postRoutes
from features.comments import routes as commentsRoutes
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(description="a blog api", title="blog")

app.include_router(userRoutes.userRouter)
app.include_router(postRoutes.postRouter)
app.include_router(commentsRoutes.commentsRouter)
