# repositories/user_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.user_model import User
from api.schemas.user_schema import UserCreate

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)  
    return db_user

async def get_user_by_email(db: AsyncSession, email: str):
    return db.query(User).filter(User.email == email).first()