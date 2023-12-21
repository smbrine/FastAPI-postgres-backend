from datetime import datetime

from pydantic import BaseModel


class AnswerBase(BaseModel):
    short_answer: str
    full_answer: str


class AnswerCreateSchema(AnswerBase):
    question_id: str
    from_id: int


class AnswerInDBSchema(AnswerBase):
    id: str
    created_at: datetime
    from_id: int
    question_id: str
    admin_approved: bool = False


class AnswerPublicSchema(AnswerBase):
    pass


class AnswerUpdateSchema(BaseModel):
    short_answer: str
    full_answer: str
