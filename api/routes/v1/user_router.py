# routes/v1/user_router.py
from fastapi import APIRouter
from api.controllers.user_controller import router as user_router

router = APIRouter(prefix="/v1")

router.include_router(user_router)