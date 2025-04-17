# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
import models
import schemas

#Task5 - Import Here
import database

app = FastAPI()

#@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

#Task5
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Task6
@app.get("/users/", response_model = List[schemas.User])
def read_users(skip: int = 0, limit:int = 100, db:Session = Depends(get_db)):
    users = crud.get_users(db, skip = skip, limit = limit)
    return users

#Task 7
@app.get("/users/{user_id}", response_model = schemas.User)
def read_user(user_id:int, db:Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id = user_id)
    if db_user is None:
        raise HTTPException
    return db_user

#Task 8
@app.get("/users/email/{user_email}", response_model= schemas.User)
def read_user_by_email(user_email:str, db:Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#Task 9
@app.post("/users/", response_model=schemas.User)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user.email)
    if db_user:
        raise HTTPException(status_code=404, detail="not found")
    return crud.create_user(db=db, user = user)
#Task 10
@app.put("/users/", response_model=schemas.User)
def update_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Email already registered")
    return crud.update_user(db, user = user)


#Task 11
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id:int, db:Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id = user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="id not exist")
    return db_user