from fastapi import APIRouter
from ...tests.test_router import router as test_router
from .user_rfid_auth_router import router as user_rfid_auth_router
from .task_auth_router import router as task_auth_router

router = APIRouter(prefix="/api/v1")

router.include_router(test_router, prefix="/test", tags=["Test"])
router.include_router(user_rfid_auth_router, prefix="/auth-rfid", tags=["Auth-RFID"])
router.include_router(task_auth_router, prefix="/tasks", tags=["Task"])
