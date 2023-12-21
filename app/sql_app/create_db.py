import asyncio

from app.sql_app.database import engine
from app.sql_app.models.base import Base


async def create_db():
    async with engine.begin() as conn:
        # noinspection PyUnresolvedReferences
        from app.sql_app.models import Question, Answer, Message, MessageContent
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()


if __name__ == '__main__':
    asyncio.run(create_db())
