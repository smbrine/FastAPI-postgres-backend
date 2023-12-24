from fastapi import APIRouter

from app.routers.v1 import LogDB
from app.sql_app.schemas.log import LogCreateSchema, LogPublicSchema

router = APIRouter(prefix="/logs", tags=["logs"])


@router.post("/add", tags=["logs"])
async def add_log(log: LogCreateSchema):
    return await LogDB.add_log(log=log)


@router.get("/{log_id}", response_model=LogPublicSchema, tags=["logs"])
async def get_log(log_id: str):
    return await LogDB.get_log(log_id=log_id)


@router.post("/paginated", tags=["logs"])
async def get_logs(page: int, page_size: int, order: str = "created_at"):
    result = await LogDB.get_paginated_logs(page, page_size, order)
    return result
