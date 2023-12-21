from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.sql_app.schemas.message_content import MessageContentPublicSchema


class MessageBase(BaseModel):
    from_id: int


class MessageCreateSchema(MessageBase):
    contents: List[MessageContentPublicSchema]


class MessageInDBSchema(MessageBase):
    id: str
    created_at: datetime
    contents: List[MessageContentPublicSchema] = []


class MessagePublicSchema(MessageBase):
    contents: List[MessageContentPublicSchema] = []


class MessageUpdateSchema(BaseModel):
    from_id: Optional[int] = None
