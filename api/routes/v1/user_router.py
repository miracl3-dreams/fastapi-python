from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.controllers.user_controller import UserController
from api.schemas.user_schema import UserCreate
from api.utils.database import get_db

router = APIRouter()
user_controller = UserController()

async def get_db():
    async with get_db() as session:
        yield session

@router.post("/create", response_model=UserCreate)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_controller.create_user(user, db)

@router.post("/login/authenticate/")
async def login_user(email: str, password: str, db: AsyncSession = Depends(get_db)):
    return await user_controller.login_user(email, password, db)
