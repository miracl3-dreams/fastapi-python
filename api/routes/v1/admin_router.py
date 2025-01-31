# routes/v1/admin_router.py
from fastapi import APIRouter
from api.controllers.admin_controller import router as admin_router

router = APIRouter(prefix="/v1")

router.include_router(admin_router)