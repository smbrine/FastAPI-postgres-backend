from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.sql_app.models.base import BaseModelDB


class Answer(BaseModelDB):
    __tablename__ = "answers"

    from_id = Column(Integer, nullable=True, index=True)
    short_answer = Column(String, nullable=False, unique=False)
    full_answer = Column(String, nullable=False, unique=True)

    admin_approved = Column(Boolean, default=False)

    question_id = Column(
        String, ForeignKey("questions.id"), nullable=False, unique=True
    )

    def __repr__(self):
        return f"<Answer to question {self.question_id}>"
