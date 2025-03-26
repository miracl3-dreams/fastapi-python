from fastapi import APIRouter
from ...tests.test_router import router as test_router
from .admin_router import router as admin_router
from .user_router import router as user_router
from .task_router import router as task_router
from .ai_agent_router import router as ai_agent_router  
from .rfid_router import router as rfid_router

router = APIRouter(prefix="/api/v1")

router.include_router(test_router, prefix="/test", tags=["Test"])
router.include_router(admin_router, prefix="/admin", tags=["Admin"])
router.include_router(user_router, prefix="/user", tags=["User"])
router.include_router(task_router, prefix="/task", tags=["Task"])
router.include_router(ai_agent_router, prefix="/ai", tags=["AI"])  
router.include_router(rfid_router, prefix="/rfid", tags=["RFID"])  
