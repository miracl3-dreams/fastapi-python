from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.models.user_model import User

class UserRepository:
    @staticmethod
    async def get_user_by_uid(db: AsyncSession, uid: str):
        result = await db.execute(select(User).filter(User.uid == uid))
        return result.scalars().first() 

    @staticmethod
    async def create_user(db: AsyncSession, user_data):
        new_user = User(**user_data.dict())
        db.add(new_user)
        await db.commit() 
        await db.refresh(new_user)
        return new_user
