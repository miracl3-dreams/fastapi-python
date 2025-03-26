from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.user_service import UserService
from api.schemas.user_schema import UserCreate
from api.utils.database import get_db

class UserController:
    @staticmethod
    async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
        user = await UserService.register_user(db, user_data)
        if not user:
            raise HTTPException(status_code=400, detail="RFID UID is already registered.")
        return user
