from sqlalchemy.orm import Session
from models import User  # SQLAlchemy 的 User 模型
from typing import List
import models
import schemas

#task6
def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return db.query(models.User).offset(skip).limit(limit).all()

# db: Session 是從 get_db() 來的 session（連線實體）
# query(User) 是查詢 User 表的意思
# offset(skip) 可以跳過前幾筆（預設是 0）
# limit(limit) 是最多撈幾筆（預設 100）
# .all() 是 SQLAlchemy 的方法，會把結果轉成 list 回傳

#task7
def get_user(db: Session, user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#task8
def get_user_by_email(db: Session, user_email:str):
    return db.query(models.User).filter(models.User.email == user_email).first()

#task9
#def create_user(db:Session, email:str, username:str, firstname:str, lastname:str, gender:str, country:str, isActive:bool):
    #db.add(email, username, firstname, lastname, gender, country, isActive)

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=fake_hashed_password,
        username = user.username,
        firstname = user.firstname,
        lastname = user.lastname,
        gender = user.gender,
        country = user.country,
        isActive = user.isActive)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#task 10
def update_user(db:Session, user:schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.emai == user.email).first()
    for field in user.__dict__:
        setattr(db_user, field, getattr(user, field))
    db.commit()
    db.refresh(db_user)
    return db_user

#task 11
def delete_user(db:Session, user_id:int):
    record_obj = db.query(models.User).filter(models.User.id == user_id).first()
    if not record_obj:
        return None
    db.delete(record_obj)
    db.commit() #把動作寫進資料庫
    return record_obj


