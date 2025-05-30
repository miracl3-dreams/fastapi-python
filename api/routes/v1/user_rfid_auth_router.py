from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.utils.database import get_db
from api.controllers.user_controller import UserController
from api.schemas.user_schema import UserCreate

router = APIRouter()
user_controller = UserController()

@router.post("/register")
async def register_rfid(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    """Register RFID of User"""
    return await user_controller.register_user(user_data, db)

@router.post("/login")
async def login_rfid(rfid_uid: str, db: AsyncSession = Depends(get_db)):
    """Authenticate user via RFID and return tokens"""
    return await user_controller.authenticate_rfid(rfid_uid, db)
