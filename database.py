from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Task-1 Code Here
# 1. 指定資料庫的路徑，這邊使用 SQLite，資料庫檔案會儲存在本地資料夾
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"

# 2. 建立 Engine，connect_args 是 SQLite 特有的設定
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3.建立 SessionLocal，供後續與資料庫互動時使用（例如在 API 中建立 session）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4.建立基底類別，後續所有資料表的模型都要繼承這個 Base
Base = declarative_base()