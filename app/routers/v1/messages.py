from fastapi import APIRouter

from app.routers.v1 import MessageDB
from app.sql_app.schemas import MessageCreateSchema, MessagePublicSchema

router = APIRouter(prefix="/messages", tags=["messages"])


@router.post("/add", response_model=MessagePublicSchema, tags=["messages"])
async def add_message(message: MessageCreateSchema):
    """
    Add a new message to the database.

    Args:
        message (MessageCreateSchema): The message to add to the database.

    Returns:
        MessagePublicSchema: The added message.
    """
    return await MessageDB.add_message(message=message)


@router.get("/{message_id}", response_model=MessagePublicSchema, tags=["messages"])
async def get_message(message_id: str):
    """
    Get a single message by its ID.

    Args:
        message_id (str): The ID of the message to retrieve.

    Returns:
        MessagePublicSchema: The retrieved message.

    Raises:
        HTTPException: If the message does not exist.
    """
    return await MessageDB.get_message(message_id=message_id)


@router.delete("/{message_id}", tags=["messages"])
async def delete_message(message_id: str):
    """
    Delete a message by its ID.

    Args:
        message_id (str): The ID of the message to delete.

    Returns:
        str: The message ID that was deleted.
    """
    return message_id
