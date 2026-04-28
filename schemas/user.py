# schemas/index.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name:     str
    email:    str
    password: str

class UserCreate(User):
    pass

class UserUpdate(BaseModel):
    name:     Optional[str] = None
    email:    Optional[str] = None
    password: Optional[str] = None