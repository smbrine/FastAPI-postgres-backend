import uuid

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.sql_app import models
from app.sql_app.crud.base import BaseCRUD

from app.sql_app.schemas import AnswerCreateSchema, AnswerPublicSchema, QuestionAnswerSchema


class AnswerCRUD(BaseCRUD):

    def __init__(self, async_session: async_sessionmaker[AsyncSession], model_class):
        super().__init__(async_session, model_class)
        self.QuestionDB = None

    def link_db(self, db):
        from app.sql_app.crud.question import QuestionCRUD
        if isinstance(db, QuestionCRUD):
            self.QuestionDB = db
        else:
            raise TypeError(f"db must be of type QuestionCRUD, not {type(db)}")

    async def add_answer(self, answer: AnswerCreateSchema):
        answer_id = str(uuid.uuid4())
        new_answer = models.Answer(
            id=answer_id, question_id=answer.question_id, from_id=answer.from_id, short_answer=answer.short_answer,
            full_answer=answer.full_answer, )

        await self._create(new_answer)

        # Create an update schema instance for Question
        question_update = QuestionAnswerSchema(answer_id=answer_id, id=answer.question_id)

        # Update the question in the database
        question_result = await self.QuestionDB.answer_question(question_update)

        if not question_result:
            return None

        # Create a response model instance from the newly created answer
        return AnswerPublicSchema(
            short_answer=new_answer.short_answer, full_answer=new_answer.full_answer
        )
