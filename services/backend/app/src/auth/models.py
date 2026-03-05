from enum import Enum

from pydantic import BaseModel, EmailStr

from app.src.base.model import CustomModel


class Role(str, Enum):
    ADMIN = "admin"
    BOARD = "board"
    PARTNER = "partner"
    USER = "user"


class User(CustomModel):
    email: EmailStr
    password: str
    is_active: bool = True
    role: Role = Role.USER


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str
