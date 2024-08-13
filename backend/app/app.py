from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
# from app.schemas import UserOut, UserAuth
from app.utils import get_hashed_password
from uuid import uuid4

# @app.post('/signup', summary = "Create new user", response_model = UserOut)
# async def create_user(data: UserAuth):
#     pass
app = FastAPI()


@app.get("/")
async def root():
    return {"message":"Hello, world"}

@app.post('/login', summary = "Create access and refresh tokens for user")
async def login():
    pass