# controllers/admin_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.admin_service import create_new_admin, authenticate_admin
from api.schemas.admin_schema import AdminCreate, AdminResponse
from api.utils.database import AsyncSessionLocal

router = APIRouter()

# Dependency to get an asynchronous database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/admins/", response_model=AdminResponse)
async def create_admin(admin: AdminCreate, db: AsyncSession = Depends(get_db)):
    return await create_new_admin(db, admin)

@router.post("/admins/authenticate/")
async def login_admin(username: str, password: str, db: AsyncSession = Depends(get_db)):
    admin = await authenticate_admin(db, username, password)
    if not admin:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}