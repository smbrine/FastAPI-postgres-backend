import uuid

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.sql_app import models
from app.sql_app.crud.base import BaseCRUD
from app.sql_app.schemas import MessageContentCreateSchema


class MessageContentCRUD(BaseCRUD):

    def __init__(self, async_session: async_sessionmaker[AsyncSession], model_class):
        super().__init__(async_session, model_class)

    async def add_message_content(self, message_content: MessageContentCreateSchema):
        message_content_obj = models.MessageContent(
            id=str(uuid.uuid4()), message_id=message_content.message_id, content=message_content.content,
            order=message_content.order, content_type=message_content.content_type, )

        return await self._create(message_content_obj)
