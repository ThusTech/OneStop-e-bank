from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from fastapi import HTTPException
from .models import Token

# ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 30 minutes
# REFRESH_TOKEN_EXPIRE_MINUTES = 60*24*7 # 7 days
# ALGORITHM = "HS256"
# JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
# JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']

password_context = CryptContext(schemes=["bcrypt"])

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

async def authenticate_user(email: str, password: str):
    if not email == 'Thulani@gmail.com':
        raise HTTPException(status_code=401, detail="Invalid email")
    
    if not password == '12345':
        return HTTPException(status_code=401, detail="Invalid Password")
    
    token = create_access_token(email=email)
    
    return Token(access_token=token, token_type="bearer")



def create_access_token(email: str):
    token = jwt.encode({"email":email}, "secret_key", algorithm="HS256")
    return token

def create_refresh_token():
    pass