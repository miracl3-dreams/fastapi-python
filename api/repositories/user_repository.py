from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.user_model import User
from api.schemas.user_schema import UserCreate
from api.utils.exceptions import EmailAlreadyExistsException

class UserRepository:
    async def create_user(self, db: AsyncSession, user_data: UserCreate):
        query = select(User).filter(User.email == user_data.email)
        result = await db.execute(query)
        existing_user = result.scalars().first()
        
        if existing_user:
            raise EmailAlreadyExistsException()

        new_user = User(**user_data.model_dump())
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    async def get_user_by_email(self, db: AsyncSession, email: str):
        query = select(User).filter(User.email == email)
        result = await db.execute(query)
        return result.scalars().first()
