# admin_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from api.database import get_database_connection

class AdminRepository:
    def __init__(self, session: AsyncSession):
        self.db = session

    async def create_admin(self, lastname: str, firstname: str, username: str, password: str) -> str:
        # Example implementation
        new_admin = {
            "lastname": lastname,
            "firstname": firstname,
            "username": username,
            "password": password
        }
        # Simulate saving to the database
        await self.db.execute("INSERT INTO admins (lastname, firstname, username, password) VALUES (:lastname, :firstname, :username, :password)", new_admin)
        await self.db.commit()
        return "Admin created successfully"
