from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.admin_model import Admin
from api.schemas.admin_schema import AdminCreate

class AdminRepository:
    async def create_admin(self, db: AsyncSession, admin_data: AdminCreate):
        new_admin = Admin(**admin_data.model_dump())
        db.add(new_admin)
        await db.commit()
        await db.refresh(new_admin)
        return new_admin

    async def get_admin_by_username(self, db: AsyncSession, username: str):
        query = select(Admin).filter(Admin.username == username)
        result = await db.execute(query)
        return result.scalars().first()
