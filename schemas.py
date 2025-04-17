from pydantic import BaseModel
from typing import List

#Task 3
class UserBase(BaseModel): #建立一個基礎的使用者資料模型
    email:str
    username:str
    firstname:str
    lastname:str
    gender:str
    country:str
    isActive:bool

#Task 4
class UserCreate(UserBase): #定義使用者註冊或建立時需要的欄位
    password: str

class User(UserBase): #用於輸出，從資料庫查到使用者後要回傳那些欄位
    id:int
    class Config:
        orm_mode = True