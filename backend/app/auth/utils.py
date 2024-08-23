from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from fastapi import HTTPException,Response,status,Request,Depends
from .models import Token, Register, Login
from .database import default_user


password_context = CryptContext(schemes=["bcrypt"])

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

async def authenticate_user(response: Response,login: Login):

    hashed_password = get_hashed_password(password="12345")
    user = Login(email="student1@wethinkcode.co.za",password=hashed_password)

    if not login.email == user.email:
        raise HTTPException(status_code=401, detail="Invalid Password or/and Email")
    
    if not verify_password(password=login.password, hashed_password=user.password):
        return HTTPException(status_code=401, detail="Invalid Password or/and Email")
    
    access_token = create_access_token(email=login.email)

    refresh_token = create_refresh_token(email=login.email)
    
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="lax"
    )
    
    return Token(access_token=access_token, token_type="bearer")

def create_access_token(email: str):
    expires_in = (datetime.now() + timedelta(minutes=15)).ctime()

    token = jwt.encode({"email":email, "exp": expires_in}, "JWT_SECRET", algorithm="HS256")

    return token

def create_refresh_token(email: str):
    expires_in = (datetime.now() + timedelta(days=3)).ctime()

    refresh_token = jwt.encode({"email":email, "exp": expires_in}, "REFRESH_TOKEN_SECRET", algorithm="HS256")

    return refresh_token

async def refresh_access_token(response: Response, request: Request):
    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token not found")
        
    try:
        payload = jwt.decode(refresh_token, "REFRESH_TOKEN_SECRET", algorithms=["HS256"])
        email = payload.get("email")

        new_access_token = create_access_token(email=email)

        return Token(access_token=new_access_token, token_type="bearer")
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token has expired")
    
async def invalidate_token(response: Response):
    response.delete_cookie(key="refresh_token")

    return Response(status_code=status.HTTP_200_OK,content="Sucessfully logged out")

async def register_new_user(register: Register):
    # Check if email/username is not in the db
    # if it is not then:
        # create a new user
        # make sure to hash the password
        # send a response with status: created
    return {"Message": "Created"}