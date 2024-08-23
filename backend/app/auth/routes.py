from fastapi import APIRouter, Depends, Response, Request
from .models import Login, Register
from .utils import authenticate_user, register_new_user, refresh_access_token, invalidate_token
from fastapi.security import OAuth2PasswordBearer, OAuth2

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post('/login', summary = "Create access and refresh tokens for user")
async def login(response: Response, login: Login):
    return await authenticate_user(response=response,login=login)

@router.post("/register", summary="Register a new user")
async def register(register: Register):
    return await register_new_user(register = register)

@router.post("/logout", summary="Log out the user and invalidate the token")
async def logout(response: Response):
    return await invalidate_token(response = response)

@router.post("/refresh-token", summary="Refresh the authentication token")
async def refresh_token(request: Request,response: Response):
    return await refresh_access_token(response=response, request=request)