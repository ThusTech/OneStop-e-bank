from fastapi import APIRouter, Depends
from .models import Login, Register
from .utils import authenticate_user, create_new_user
from fastapi.security import OAuth2PasswordBearer, OAuth2

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post('/login', summary = "Create access and refresh tokens for user")
async def login(login: Login):
    return await authenticate_user(login=login)

@router.post("/register", summary="Register a new user")
async def register(register: Register):
    return await create_new_user(register = register)

@router.post("/logout", summary="Log out the user and invalidate the token")
async def logout():
    pass

@router.post("/refresh-token", summary="Refresh the authentication token")
async def refresh_token():
    pass