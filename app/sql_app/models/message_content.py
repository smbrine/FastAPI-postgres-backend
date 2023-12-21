from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.sql_app.models.base import BaseModelDB


class MessageContent(BaseModelDB):
    __tablename__ = "message_contents"

    message_id = Column(String, ForeignKey('messages.id'))
    content = Column(String, nullable=False)
    order = Column(Integer, nullable=False)

    content_type = Column(String, default='text')

    message = relationship("Message", back_populates="contents")

    def __repr__(self):
        return f"<MessageContent of type {self.content_type} for message {self.message_id}>"
