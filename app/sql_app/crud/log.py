import uuid

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.sql_app import models
from app.sql_app.crud.base import BaseCRUD
from app.sql_app.schemas import LogCreateSchema, LogPublicSchema


class LogCRUD(BaseCRUD):
    def __init__(
        self, async_session: async_sessionmaker[AsyncSession], model_class
    ) -> None:
        super().__init__(async_session, model_class)

    async def add_log(self, log: LogCreateSchema) -> models.Log:
        """
        Adds a log to the LogDB and returns the models.Log instance
        :param log: Log to add in a LogCreateSchema type
        :return: added to the db models.Log instance
        """
        new_log = models.Log(
            id=str(uuid.uuid4()),
            **log.model_dump(),
        )
        result = await self._create(new_log)
        return result

    async def get_log(self, log_id: str):
        log = await self._get_one("id", log_id)
        log = log.scalars().one_or_none()

        if not log:
            return None

        return LogPublicSchema(**log.dict())

    async def get_paginated_logs(
        self, page: int, per_page: int, order: str = "created_at"
    ):
        logs = await self._get_paginated(page, per_page, order)
        logs = logs.scalars().all()
        if not logs:
            return None

        log_public_schemas = []

        for log in logs:
            log_data = LogPublicSchema(**log.dict())
            log_public_schemas.append(log_data)

        return log_public_schemas
