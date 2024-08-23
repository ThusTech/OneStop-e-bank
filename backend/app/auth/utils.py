from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from fastapi import HTTPException
from .models import Token, Register, Login
from .database import default_user


password_context = CryptContext(schemes=["bcrypt"])

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

async def authenticate_user(login: Login):

    hashed_password = get_hashed_password(password="12345")
    user = Login(email="student1@wethinkcode.co.za",password=hashed_password)

    if not login.email == user.email:
        raise HTTPException(status_code=401, detail="Invalid Password or/and Email")
    
    if not verify_password(password=login.password, hashed_password=user.password):
        return HTTPException(status_code=401, detail="Invalid Password or/and Email")
    
    access_token, expires_in = create_access_token(email=login.email)

    # refresh token
    # refresh_token = create_refresh_token()
    
    # login.set_cookie(
    #     key="refresh_token",
    #     value=refresh_token,
    #     httponly=True,
    #     secure=True,
    #     samesite="Lax"
    # )
    
    return Token(access_token=access_token, token_type="bearer", expires_in=expires_in)

def validate_tokens():
    # Check if access_token, and refresh_token are expired
    # If access_token is expired: Create another token using refresh token
    # If both access_token and refresh token are expired, tell the user to login again
    pass

def create_access_token(email: str):
    token = jwt.encode({"email":email}, "secret_key", algorithm="HS256")
    expires_in = (datetime.now() + timedelta(minutes=15)).ctime()

    return token, expires_in

def create_refresh_token():
    # token = jwt.encode({"email":email}, "secret_key", algorithm="HS256")
    expires_in = (datetime.now() + timedelta(hours=24)).ctime()
    # return refresh_token, expires_in

    
    
    # return token, expires_in

async def register_new_user(register: Register):
    # Check if email/username is not in the db
    # if it is not then:
        # create a new user
        # make sure to hash the password
        # send a response with status: created
    return {"Message": "Created"}