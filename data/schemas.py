from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class User(BaseModel):
    phone: str
    email: str
    name: str
    surname: str
    age: int
    password: str
    about: str

    class Config:
        orm_mode = True


class Achievement(BaseModel):
    author: int
    name: str
    post_datetime: datetime
    description: str


class Skill(BaseModel):
    author: int
    name: str


class Contact(BaseModel):
    author: int
    text: str
    link: str
