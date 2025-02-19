from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.admin_service import AdminService
from api.schemas.admin_schema import AdminCreate, AdminResponse
from api.utils.custom_error import AuthError
from api.utils.handle_exception import handle_exception
from api.utils.app_response import AppResponse

class AdminController:
    def __init__(self):
        self.admin_service = AdminService()

    async def create_admin(self, admin_data: AdminCreate, db: AsyncSession) -> dict:
        """Create a new admin."""
        try:
            admin = await self.admin_service.create_new_admin(db, admin_data)
            admin_response = AdminResponse.model_validate(admin)
            return AppResponse.send_success(
                message="Admin created successfully", 
                data=admin_response.model_dump()  
            )
        except AuthError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except HTTPException as e:
            raise e
        except Exception as e:
            return handle_exception(e)

    async def login_admin(self, email: str, password: str, db: AsyncSession) -> dict:
        """Login admin."""
        try:
            admin = await self.admin_service.authenticate_admin(db, email, password)
            if not admin:
                raise AuthError()
            return AppResponse.send_success(message="Login successful as Admin", data={})
        except AuthError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except HTTPException as e:
            raise e
        except Exception as e:
            return handle_exception(e)
