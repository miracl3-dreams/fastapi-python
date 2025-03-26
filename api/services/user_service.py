from sqlalchemy.ext.asyncio import AsyncSession
from api.repositories.user_repository import UserRepository
from api.schemas.user_schema import UserCreate

class UserService:
    @staticmethod
    async def register_user(db: AsyncSession, user_data: UserCreate):
        existing_user = await UserRepository.get_user_by_uid(db, user_data.uid)
        if existing_user:
            return None 
        return await UserRepository.create_user(db, user_data)
