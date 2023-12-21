from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.sql_app.models.base import BaseModelDB


class Message(BaseModelDB):
    __tablename__ = "messages"

    from_id = Column(Integer, index=True)

    contents = relationship("MessageContent", back_populates="message", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Message from {self.from_id} sent {self.created_at}>"
