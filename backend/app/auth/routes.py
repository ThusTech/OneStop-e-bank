from fastapi import APIRouter, Depends
from .models import Login
from .utils import authenticate_user
from fastapi.security import OAuth2PasswordBearer, OAuth2

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post('/login', summary = "Create access and refresh tokens for user")
async def login(login: Login):
    return await authenticate_user(email = login.email, password=login.password)

@router.post("/refresh", summary="Refresh token endpoint")
async def refresh(token: str = Depends(oauth2_scheme)):
    pass