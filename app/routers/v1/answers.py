from fastapi import APIRouter

from app.routers.v1 import AnswerDB
from app.sql_app.schemas.answer import AnswerCreateSchema, AnswerPublicSchema

router = APIRouter(prefix="/answers", tags=["answers"])


@router.post("/add", response_model=AnswerPublicSchema, tags=["answers"])
async def add_answer(answer: AnswerCreateSchema):
    """
    This function adds a new answer to the database.

    Args:
        answer (AnswerCreateSchema): The answer to be added to the database.

    Returns:
        AnswerPublicSchema: The newly added answer.
    """
    return await AnswerDB.add_answer(answer=answer)
