from fastapi import APIRouter
from .test_router import router as test_router
from .admin_router import router as admin_router
from .user_router import router as user_router
from .task_router import router as task_router

router = APIRouter(prefix="/api/v1")

router.include_router(test_router, prefix="/test", tags=["Test"])
router.include_router(admin_router, prefix="/admin", tags=["Admin"])
router.include_router(user_router, prefix="/user", tags=["User"])
router.include_router(task_router, prefix="/task", tags=["Task"])
