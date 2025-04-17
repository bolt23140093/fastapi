from sqlalchemy import Boolean, Column, Integer, String
from database import Base, engine

#Task2 - Code Here
class User(Base):
    __tablename__ = "Users" #指定資料表名稱(必要)
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    country = Column(String, nullable=False)
    isActive = Column(Boolean, default=True)
    hashed_password = Column(String, nullable=False)

Base.metadata.create_all(engine)
