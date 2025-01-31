# repositories/admin_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from api.models.admin_model import Admin
from api.schemas.admin_schema import AdminCreate

async def create_admin(db: AsyncSession, admin: AdminCreate):
    db_admin = Admin(username=admin.username, password=admin.password)
    db.add(db_admin)
    await db.commit()
    await db.refresh(db_admin)
    return db_admin

async def get_admin_by_username(db: Session, username: str):
    return db.query(Admin).filter(Admin.username == username).first()