from datetime import datetime

from pydantic import BaseModel


class MessageContentBase(BaseModel):
    content: str
    order: int
    content_type: str


class MessageContentCreateSchema(BaseModel):
    message_id: str
    content: str
    order: int
    content_type: str


class MessageContentInDBSchema(MessageContentBase):
    id: str
    created_at: datetime
    message_id: str


class MessageContentPublicSchema(MessageContentBase):
    pass
