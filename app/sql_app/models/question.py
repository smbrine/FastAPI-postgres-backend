from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.sql_app.models.base import BaseModelDB


class Question(BaseModelDB):
    __tablename__ = "questions"

    from_id = Column(Integer, nullable=True, index=True)

    title = Column(String, unique=True, index=True)
    description = Column(String, unique=False, index=True)
    admin_approved = Column(Boolean, default=False)

    answer_id = Column(String, ForeignKey('answers.id', ondelete='CASCADE'), nullable=True, unique=True, )

    def __repr__(self):
        return (f"<Question {self.title} from {self.from_id}. "
                f"Is {'' if self.admin_approved else 'not'} approved by admin>")
