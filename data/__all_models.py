import datetime
import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class Achievement(SqlAlchemyBase):
    __tablename__ = 'achievements'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    author = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    name = sa.Column(sa.Text)
    post_datetime = sa.Column(sa.Date)
    description = sa.Column(sa.Text)


class Skill(SqlAlchemyBase):
    __tablename__ = 'skills'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    author = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    name = sa.Column(sa.Text)


class Contact(SqlAlchemyBase):
    __tablename__ = 'skills'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    author = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    name = sa.Column(sa.Text)
    link = sa.Column(sa.Text)


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    phone = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    email = sa.Column(sa.String)
    password = sa.Column(sa.String)
    about = sa.Column(sa.String)