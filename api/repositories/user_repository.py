from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.models.user_model import User
from api.schemas.user_schema import UserCreate  

class UserRepository:
    def __init__(self):
        pass  

    async def get_user_by_uid(self, db: AsyncSession, uid: str) -> User | None:
        result = await db.execute(select(User).filter(User.uid == uid))
        return result.scalars().first()

    async def create_user(self, db: AsyncSession, user_data: UserCreate) -> User:
        new_user = User(**user_data.model_dump())  
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user
