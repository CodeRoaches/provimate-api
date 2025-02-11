from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ
from ..schemas.config import settings

username = settings.database_username
password = settings.database_password
hostname = settings.database_hostname
database_name = settings.database_name
database_port = settings.database_port

RAW_DATABASE_URL = f"postgresql://{username}:{password}@{hostname}:{database_port}/{database_name}"

DATABASE_URL = f"{RAW_DATABASE_URL}_test" if environ.get("TESTING") else RAW_DATABASE_URL


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
