from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.controllers.admin_controller import AdminController
from api.schemas.admin_schema import AdminCreate
from api.utils.database import AsyncSessionLocal

router = APIRouter()
admin_controller = AdminController()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/create", response_model=AdminCreate)
async def create_admin(admin: AdminCreate, db: AsyncSession = Depends(get_db)):
    return await admin_controller.create_admin(admin, db)

@router.post("/login/authenticate/")
async def login_admin(email: str, password: str, db: AsyncSession = Depends(get_db)):
    return await admin_controller.login_admin(email, password, db)
