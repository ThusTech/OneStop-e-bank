from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60*24*7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']

password_context = CryptContext(schemes=["bcrypt"])

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

def create_access_token():
    pass

def create_refresh_token():
    pass


# hashed = "$2b$12$BS360F36b7TpC0e2GgVhs.dIf4QlaQnT8JM0Wd3Eakz7mQ0T50eiO"

# print(verify_password(password="Thulani", hashed_password=hashed))