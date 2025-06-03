from sqlalchemy.ext.asyncio import AsyncSession
from api.utils.app_response import AppResponse
from api.services.user_service import UserService
from api.schemas.user_schema import UserCreate
from api.utils.handle_exception import handle_exception

class UserController:
    """
    Controller for handling user registration and authentication.
    """

    def __init__(self):
        self.user_service = UserService()  

    async def register_user(self, user_data: UserCreate, db: AsyncSession):
        """Registers a new user using RFID."""
        try:
            user = await self.user_service.register_user(db, user_data)
            return AppResponse.send_success(
                data={"user_id": user.id, "rfid_uid": user.rfid_uid},
                message="User registered successfully."
            )
        except Exception as e:
            return handle_exception(e)

    async def authenticate_rfid(self, rfid_uid: str, db: AsyncSession):
        """Authenticates a user using RFID UID and generates tokens."""
        try:
            tokens = await self.user_service.authenticate_rfid(db, rfid_uid)
            return AppResponse.send_success(
                data=tokens,
                message="User authenticated successfully."
            )
        except Exception as e:
            return handle_exception(e)
