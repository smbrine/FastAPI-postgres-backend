from fastapi import APIRouter

from app.routers.v1 import MessageDB
from app.sql_app.schemas import MessageCreateSchema, MessagePublicSchema

router = APIRouter(prefix="/messages", tags=["messages"])


@router.post('/add', response_model=MessagePublicSchema, tags=["messages"])
async def add_message(message: MessageCreateSchema):
    return await MessageDB.add_message(message=message)


@router.get('/{message_id}', response_model=MessagePublicSchema, tags=["messages"])
async def get_message(message_id: str):
    return await MessageDB.get_message(message_id=message_id)


@router.delete('/{message_id}', tags=["messages"])
async def delete_message(message_id: str):
    return message_id
