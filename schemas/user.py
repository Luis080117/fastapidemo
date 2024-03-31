from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    username: str
    email: str
    password: str
    is_active: bool

class User(UserBase):
    username: str
    email: str
    password: str
    is_active: bool

    class Config:
        orm_mode = True
