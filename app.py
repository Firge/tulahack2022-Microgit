from fastapi import FastAPI, HTTPException
from data import db_session
from data.__all_models import User, Contact, Achievement, Skill
from data import schemas

app = FastAPI()
db_session.global_init('db/blogs.db')


@app.get('/api/get_portfolio/{user_id}')
async def get_portfolio(user_id: int):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    achievements = session.query(Achievement).filter(Achievement.author == user_id).all()
    contacts = session.query(Contact).filter(Contact.author == user_id).all()
    skills = session.query(Skill).filter(Skill.author == user_id).all()
    if not user:
        raise HTTPException(404, 'User not found')
    return [achievements, contacts, skills, user]


@app.delete('/api/delete_user/{user_id}')
async def delete_user(user_id: int):
    session = db_session.create_session()
    user = session.query(User).filter_by(id=user_id)
    if not user:
        raise HTTPException(400, 'User not exists')
    user.delete()
    session.commit()
    return 'Ok'


@app.post('/api/change_user/{user_id}', response_model=schemas.User)
async def change_user(user_id: int, new_user: schemas.User):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        raise HTTPException(400, 'User not exists')
    user.update(new_user)
    session.commit()
    return session.query(User).get(user_id)


@app.post('/api/reg_user', response_model=schemas.User)
async def reg_user(new_user: schemas.User):
    new_user = User(**new_user.dict())
    session = db_session.create_session()
    session.add(new_user)
    session.commit()
    return 'Ok'


@app.post('/api/add_contact', response_model=schemas.Contact)
async def add_contact(new_contact: schemas.Contact):
    new_contact = Contact(**new_contact.dict())
    session = db_session.create_session()
    session.add(new_contact)
    session.commit()
    return 'Ok'


@app.post('/api/add_skill', response_model=schemas.Skill)
async def add_skill(new_skill: schemas.Skill):
    new_skill = Skill(**new_skill.dict())
    session = db_session.create_session()
    session.add(new_skill)
    session.commit()
    return 'Ok'


@app.post('/api/add_achievement', response_model=schemas.Achievement)
async def add_achievement(new_article: schemas.Achievement):
    new_article = Achievement(**new_article.dict())
    session = db_session.create_session()
    session.add(new_article)
    session.commit()
    return 'Ok'


@app.get('/')
async def start_page():
    return 'Hello!'
