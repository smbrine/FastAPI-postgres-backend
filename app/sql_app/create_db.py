import asyncio
import os
import sys

this_path = str(os.path.abspath(os.path.dirname(__file__))).replace("/app/sql_app", "")
sys.path.append(this_path)
from app.sql_app.database import engine
from app.sql_app.models.base import Base


async def create_db():
    async with engine.begin() as conn:
        # noinspection PyUnresolvedReferences
        from app.sql_app.models import Question, Answer, Message, MessageContent, Log

        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(create_db())
