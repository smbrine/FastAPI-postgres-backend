import uuid

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.orm import joinedload

from app.sql_app import models
from app.sql_app.crud.base import BaseCRUD
from app.sql_app.schemas import (
    MessageContentPublicSchema,
    MessageCreateSchema,
    MessagePublicSchema,
)


class MessageCRUD(BaseCRUD):
    def __init__(self, async_session: async_sessionmaker[AsyncSession], model_class):
        super().__init__(async_session, model_class)
        self.MessageContentDB = None

    def link_db(self, db):
        from app.sql_app.crud.message_content import MessageContentCRUD

        if isinstance(db, MessageContentCRUD):
            self.MessageContentDB = db
        else:
            raise TypeError(f"db must be of type QuestionCRUD, not {type(db)}")

    async def add_message(self, message: MessageCreateSchema):
        new_message_id = str(uuid.uuid4())
        new_message = models.Message(id=new_message_id, from_id=message.from_id)
        message_obj = await self._create(new_message)

        if not message_obj:
            raise HTTPException(status_code=501)

        new_contents = [
            models.MessageContent(
                id=str(uuid.uuid4()),
                message_id=new_message_id,
                content=content.content,
                order=content.order,
                content_type=content.content_type,
            )
            for content in message.contents
        ]

        message_contents_obj = []

        for message_content in new_contents:
            message_content_obj = await self.MessageContentDB.add_message_content(
                message_content
            )
            if not message_content_obj:
                raise HTTPException(status_code=501)
            message_contents_obj.append(message_content_obj)

        return_contents = [
            MessageContentPublicSchema(
                content=message_content.content,
                order=message_content.order,
                content_type=message_content.content_type,
            )
            for message_content in message_contents_obj
        ]

        return MessagePublicSchema(from_id=message.from_id, contents=return_contents)

    async def get_message(self, message_id: str):
        options = [joinedload(models.Message.contents)]
        message = await self._get_one("id", message_id, options)
        message = message.unique()
        return message.scalars().one_or_none()
