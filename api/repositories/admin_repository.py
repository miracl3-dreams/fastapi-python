from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.admin_model import Admin
from api.schemas.admin_schema import AdminCreate
from api.utils.exceptions import EmailAlreadyExistsException

class AdminRepository:
    async def create_admin(self, db: AsyncSession, admin_data: AdminCreate) -> Admin:
        query = select(Admin).filter(Admin.email == admin_data.email)
        result = await db.execute(query)
        existing_admin = result.scalars().first()

        if existing_admin:
            raise EmailAlreadyExistsException()

        new_admin = Admin(**admin_data.model_dump())
        db.add(new_admin)
        await db.commit()
        await db.refresh(new_admin)
        return new_admin

    async def get_admin_by_email(self, db: AsyncSession, email: str) -> Admin | None:
        query = select(Admin).filter(Admin.email == email)
        result = await db.execute(query)
        return result.scalars().first()
