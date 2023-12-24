from datetime import datetime

from pydantic import BaseModel


class LogBase(BaseModel):
    level: str
    message: str
    filename: str


class LogCreateSchema(LogBase):
    pass


class LogInDBSchema(LogBase):
    id: str
    created_at: datetime


class LogPublicSchema(LogBase):
    created_at: datetime
