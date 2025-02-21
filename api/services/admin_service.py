from fastapi import HTTPException
from api.repositories.admin_repository import AdminRepository
from api.schemas.admin_schema import AdminCreate, AdminResponse
from api.utils.password import PasswordManager 
from api.utils.custom_error import AuthError
from api.utils.exceptions import EmailAlreadyExistsException
from sqlalchemy.ext.asyncio import AsyncSession

class AdminService:
    def __init__(self):
        self.admin_repository = AdminRepository()

    async def create_new_admin(self, db: AsyncSession, admin_data: AdminCreate) -> AdminResponse:
        """Hash the password using PasswordManager"""
        hashed_password = PasswordManager.hash_password(admin_data.password)  
        admin_data.password = hashed_password
        
        """Create admin."""
        try:
            admin = await self.admin_repository.create_admin(db, admin_data)
        except EmailAlreadyExistsException:
            raise EmailAlreadyExistsException()
        return AdminResponse.model_validate(admin)

    async def authenticate_admin(self, db: AsyncSession, email: str, password: str) -> AdminResponse: 
        """Logging the Admin"""
        admin = await self.admin_repository.get_admin_by_email(db, email)
        if admin and PasswordManager.verify_password(password, admin.password): 
            return AdminResponse.model_validate(admin)
        raise AuthError()
