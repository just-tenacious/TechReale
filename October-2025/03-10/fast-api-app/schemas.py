from pydantic import BaseModel, EmailStr, constr
from datetime import date
from typing import Optional, List

class UserCreate(BaseModel):
    name: str
    dob: date
    address: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
    address: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserOut(BaseModel):
    user_id: int
    name: str
    dob: date
    address: str
    email: EmailStr

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class PasswordChangeRequest(BaseModel):
    old_password: constr(min_length=6)
    new_password: constr(min_length=6)

class PostCreate(BaseModel):
    post: str

class PostOut(BaseModel):
    pid: int
    post: str
    response: Optional[str] = None
    uid: int

    class Config:
        from_attributes = True

class AdminPostQueryOut(BaseModel):
    pid: int
    uid: int
    post: str
    response: Optional[str] = None  

    class Config:
        from_attributes = True

class AdminPostResponse(BaseModel):
    response: constr(min_length=1, max_length=1000)