# controllers/user_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.user_service import create_new_user, authenticate_user
from api.schemas.user_schema import UserCreate, UserResponse
from api.utils.database import AsyncSessionLocal

router = APIRouter()

# Dependency to get an asynchronous database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_new_user(db, user)

@router.post("/users/authenticate/")
async def login_user(email: str, password: str, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}