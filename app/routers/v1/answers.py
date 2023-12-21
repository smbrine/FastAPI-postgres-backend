from fastapi import APIRouter

from app.routers.v1 import AnswerDB
from app.sql_app.schemas.answer import AnswerCreateSchema, AnswerPublicSchema

router = APIRouter(prefix="/answers", tags=["answers"])


@router.post('/add', response_model=AnswerPublicSchema, tags=["answers"])
async def add_answer(answer: AnswerCreateSchema):
    return await AnswerDB.add_answer(answer=answer)
