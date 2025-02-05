from api.repositories.admin_repository import AdminRepository
from api.schemas.admin_schema import AdminCreate, AdminResponse
from api.utils.encryption import hash_password, verify_password
from api.utils.custom_error import AuthError
from sqlalchemy.ext.asyncio import AsyncSession

class AdminService:
    def __init__(self, admin_repository: AdminRepository = AdminRepository()):
        self.admin_repository = admin_repository

    async def create_new_admin(self, db: AsyncSession, admin_data: AdminCreate) -> AdminResponse:
        # Hash the password before storing
        hashed_password = hash_password(admin_data.password)
        admin_data.password = hashed_password
        # Store the new admin using the repository
        admin = await self.admin_repository.create_admin(db, admin_data)
        return AdminResponse.model_validate(admin)  
    
    async def authenticate_admin(self, db: AsyncSession, username: str, password: str) -> AdminResponse:
        # Fetch the admin by username
        admin = await self.admin_repository.get_admin_by_username(db, username)
        if admin and verify_password(password, admin.password):
            return AdminResponse.model_validate(admin)
        raise AuthError("Invalid credentials")
