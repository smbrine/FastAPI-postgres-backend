"""
Main router. Handles all the /v1 requests.
"""
from fastapi import APIRouter
from app.routers.v1 import answers, messages, questions, logs

router = APIRouter(prefix="/v1")

router.include_router(answers.router)
router.include_router(messages.router)
router.include_router(questions.router)
router.include_router(logs.router)
