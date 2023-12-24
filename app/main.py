from fastapi import FastAPI

from app.routers import main_router

from app.sql_app.create_db import create_db
from sqlalchemy.exc import CircularDependencyError
import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(
    app: FastAPI,
):
    try:
        await create_db()
        print("Database created successfully")
    except CircularDependencyError as e:
        message = f"Seems like database is already created. If not, here's an error from which it was decided that tables exist:\n{e}"
        print(message)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(main_router.router, prefix="/api")
