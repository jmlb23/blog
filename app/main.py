from fastapi import FastAPI
from features.users import routes


app = FastAPI()
app.include_router(routes.userRouter)
