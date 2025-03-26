from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.controllers.user_controller import UserController
from api.schemas.user_schema import UserCreate
from api.utils.database import get_db

router = APIRouter()

@router.post("/rfid/register")
async def register_user(user_data: UserCreate, db: Session = Depends(get_db)):  
    return await UserController.register_user(user_data, db) 
