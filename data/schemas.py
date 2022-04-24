from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class User(BaseModel):
    phone: str
    email: EmailStr
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


class Comment(BaseModel):
    author: str
    text: str
    post_datetime: datetime
    article_id: int
