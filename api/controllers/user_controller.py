from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.user_service import UserService
from api.schemas.user_schema import UserCreate
from api.utils.database import get_db

class UserController:
    def __init__(self):
        self.user_service = UserService()  

    async def register_user(self, user_data: UserCreate, db: AsyncSession):
        """Create a user using RFID."""
        user = await self.user_service.register_user(db, user_data)
        if not user:
            raise HTTPException(status_code=400, detail="RFID UID is already registered.")
        return user
