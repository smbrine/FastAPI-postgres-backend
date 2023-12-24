from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.sql_app.models.base import BaseModelDB


class Log(BaseModelDB):
    __tablename__ = "logs"

    level = Column(String, nullable=False)
    message = Column(String, nullable=False)
    filename = Column(String, nullable=True)

    def __repr__(self):
        return f"<Log |{self.id}| {self.level}: {self.message} at |{self.created_at}|>"
