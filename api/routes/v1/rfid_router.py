from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.controllers.user_controller import UserController
from api.schemas.user_schema import UserCreate
from api.utils.database import get_db

router = APIRouter()
user_controller = UserController()  

@router.post("/register")
async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):  
    return await user_controller.register_user(user_data, db)  
