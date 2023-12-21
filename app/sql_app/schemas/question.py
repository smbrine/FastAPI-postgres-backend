from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.sql_app.schemas.answer import AnswerPublicSchema


class QuestionBase(BaseModel):
    title: str
    description: str


class QuestionCreateSchema(QuestionBase):
    from_id: int


class QuestionInDBSchema(QuestionBase):
    id: str
    created_at: datetime
    from_id: int

    admin_approved: bool


class QuestionPublicSchema(QuestionBase):
    id: str
    admin_approved: bool
    answer: Optional[AnswerPublicSchema] = None


class QuestionUpdateSchema(QuestionBase):
    id: str
    answer_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None


class QuestionAnswerSchema(BaseModel):
    id: str
    answer_id: str
