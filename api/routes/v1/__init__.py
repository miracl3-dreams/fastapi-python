from fastapi import APIRouter
from ...tests.test_router import router as test_router
from .rfid_auth_router import router as rfid_auth_router
from .ai_agent_router import router as ai_agent_router

router = APIRouter(prefix="/api/v1")

router.include_router(test_router, prefix="/test", tags=["Test"])
router.include_router(rfid_auth_router, prefix="/auth/rfid", tags=["Authentication for RFID"])
router.include_router(ai_agent_router, prefix="/ai", tags=["Artifical Intelligence for Tasks"])
