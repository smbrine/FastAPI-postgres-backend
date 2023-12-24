import uuid

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.sql_app import models
from app.sql_app.crud.base import BaseCRUD
from app.sql_app.schemas import (
    AnswerPublicSchema,
    QuestionAnswerSchema,
    QuestionCreateSchema,
    QuestionPublicSchema,
)


class QuestionCRUD(BaseCRUD):
    def __init__(
        self, async_session: async_sessionmaker[AsyncSession], model_class
    ) -> None:
        super().__init__(async_session, model_class)
        self.AnswerDB = None

    def link_db(self, db) -> None:
        """
        Links the AnswerDB to the QuestionDB
        :param db: AnswerCRUD database
        """
        from app.sql_app.crud.answer import AnswerCRUD

        if isinstance(db, AnswerCRUD):
            self.AnswerDB = db
        else:
            raise TypeError(f"db must be of type AnswerCRUD, not {type(db)}")

    async def add_question(self, question: QuestionCreateSchema) -> models.Question:
        """
        Adds a question to the QuestionDB and returns the models.Question instance
        :param question: Question to add in a QuestionCreateSchema type
        :return: added to the db models.Question instance
        """
        new_question = models.Question(
            id=str(uuid.uuid4()),
            title=question.title,
            description=question.description,
            from_id=question.from_id,
        )
        result = await self._create(new_question)
        return result

    async def get_question(self, question_id: str):
        question = await self._get_one("id", question_id)
        question = question.scalars().one_or_none()

        if not question:
            return None

        answer_data = None
        if question.answer_id:
            answer = await self.AnswerDB._get_one("id", question.answer_id)
            answer = answer.scalars().one_or_none()

            if answer:
                answer_data = AnswerPublicSchema(
                    short_answer=answer.short_answer, full_answer=answer.full_answer
                )

        return QuestionPublicSchema(
            id=question.id,
            title=question.title,
            description=question.description,
            answer=answer_data,
            admin_approved=question.admin_approved,
        )

    async def get_paginated_questions(
        self, page: int, per_page: int, order: str = "created_at"
    ):
        questions = await self._get_paginated(page, per_page, order)
        questions = questions.scalars().all()
        if not questions:
            return None

        question_public_schemas = []

        for question in questions:
            answer_data = None
            if question.answer_id:
                answer = await self.AnswerDB._get_one("id", question.answer_id)

                answer = answer.scalars().one_or_none()

                if answer:
                    answer_data = AnswerPublicSchema(
                        short_answer=answer.short_answer, full_answer=answer.full_answer
                    )

            question_data = QuestionPublicSchema(
                id=question.id,
                title=question.title,
                description=question.description,
                answer=answer_data,
                admin_approved=question.admin_approved
                if question.admin_approved
                else False,
            )
            question_public_schemas.append(question_data)

        return question_public_schemas

    async def answer_question(self, question: QuestionAnswerSchema):
        result = await self._update(question)
        return result
