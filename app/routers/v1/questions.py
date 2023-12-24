from fastapi import APIRouter

from app.routers.v1 import QuestionDB
from app.sql_app.schemas.question import QuestionCreateSchema, QuestionPublicSchema

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post("/add", tags=["questions"])
async def add_question(question: QuestionCreateSchema):
    return await QuestionDB.add_question(question=question)


@router.get("/{question_id}", response_model=QuestionPublicSchema, tags=["questions"])
async def get_question(question_id: str):
    return await QuestionDB.get_question(question_id=question_id)


@router.post("/paginated", tags=["questions"])
async def get_questions(page: int, page_size: int, order: str = "created_at"):
    result = await QuestionDB.get_paginated_questions(page, page_size, order)
    return result
