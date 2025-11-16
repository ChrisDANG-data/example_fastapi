from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import psycopg
import time
from psycopg.rows import dict_row
from .config import settings


SQLALCHEMY_DATBASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"


engine = create_engine(SQLALCHEMY_DATBASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:

#     try:
#         conn = psycopg.connect(host="localhost", dbname="FastAPI", user="postgres", password="20170418",port=5432, row_factory=dict_row)
#         cursor = conn.cursor()
#         print("is able to connect ")
#         break
#     except Exception as error:
#         print("failed to connect")
#         print(error)
#         time.sleep(3)



