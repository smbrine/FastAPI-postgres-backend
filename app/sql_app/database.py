import os

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

load_dotenv()

SQLALCHEMY_DATABASE_URL = sqlalchemy.URL.create(
    drivername=os.getenv("SQL_DRIVER"),
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

session = async_sessionmaker(bind=engine, expire_on_commit=False)
