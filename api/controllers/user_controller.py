from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.user_service import UserService
from api.schemas.user_schema import UserCreate, UserResponse
from api.utils.custom_error import AuthError
from api.utils.handle_exception import handle_exception

class UserController:
    def __init__(self):
        self.user_service = UserService()

    async def create_user(self, user_data: UserCreate, db: AsyncSession):
        try:
            user = await self.user_service.create_new_user(db, user_data)
            return user
        except AuthError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            return handle_exception(e)

    async def login_user(self, email: str, password: str, db: AsyncSession):
        try:
            user = await self.user_service.authenticate_user(db, email, password)
            if not user:
                raise AuthError("Invalid credentials")
            return {"message": "Login successful as User"}
        except AuthError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            return handle_exception(e)
