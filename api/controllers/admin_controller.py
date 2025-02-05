from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.admin_service import AdminService
from api.schemas.admin_schema import AdminCreate, AdminResponse
from api.utils.custom_error import AuthError
from api.utils.handle_exception import handle_exception

class AdminController:
    def __init__(self):
        self.admin_service = AdminService()

    async def create_admin(self, admin_data: AdminCreate, db: AsyncSession):
        try:
            admin = await self.admin_service.create_new_admin(db, admin_data)
            return admin
        except AuthError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            return handle_exception(e)

    async def login_admin(self, username: str, password: str, db: AsyncSession):
        try:
            admin = await self.admin_service.authenticate_admin(db, username, password)
            if not admin:
                raise AuthError("Invalid credentials")
            return {"message": "Login successful as Admin"}
        except AuthError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            return handle_exception(e)
