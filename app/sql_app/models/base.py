from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class BaseModelDB(Base):
    __abstract__ = True
    id = Column(String, primary_key=True)
    created_at = Column(DateTime, default=datetime.now, index=True)
