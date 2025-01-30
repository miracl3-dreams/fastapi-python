# admin_service.py
from api.repositories.admin_repository import AdminRepository
from api.database import get_database_connection

class AdminService:
    def __init__(self):
        # Get the database session here and pass it to AdminRepository
        self.db_session = get_database_connection()  # Adjust based on your implementation
        self.admin_repository = AdminRepository(self.db_session)

    async def create_admin(self) -> str:
        message = await self.admin_repository.create_admin()
        return message
