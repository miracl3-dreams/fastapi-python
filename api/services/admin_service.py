from fastapi import HTTPException
from api.repositories.admin_repository import AdminRepository
from api.schemas.admin_schema import AdminCreate, AdminResponse
from api.utils.encryption import hash_password, verify_password
from api.utils.custom_error import AuthError
from api.utils.exceptions import EmailAlreadyExistsException
from sqlalchemy.ext.asyncio import AsyncSession

class AdminService:
    def __init__(self):
        self.admin_repository = AdminRepository()

    async def create_new_admin(self, db: AsyncSession, admin_data: AdminCreate):
        hashed_password = hash_password(admin_data.password)
        admin_data.password = hashed_password
        
        try:
            admin = await self.admin_repository.create_admin(db, admin_data)
        except EmailAlreadyExistsException as e:
            raise EmailAlreadyExistsException()  
        return admin  
        
    async def authenticate_admin(self, db: AsyncSession, email: str, password: str):
        admin = await self.admin_repository.get_admin_by_email(db, email)
        if admin and verify_password(password, admin.password):
            return admin
        raise AuthError()
