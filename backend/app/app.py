from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from uuid import uuid4
from .auth.routes import router as auth_router


app = FastAPI()


# Authentication routes
app.include_router(auth_router, prefix="/auth")

# @app.post('/signup', summary = "Create new user", response_model = UserOut)
# async def create_user(data: UserAuth):
#     pass