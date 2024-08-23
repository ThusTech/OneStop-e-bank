from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str

class Register(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str
    password: str
    verify_password: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: str | None = None