from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.utils.app_response import AppResponse
from api.services.user_service import UserService
from api.schemas.user_schema import UserCreate
# from api.utils.database import get_db

class UserController:
    """
    Controller for handling user registration and authentication.
    """

    def __init__(self):
        self.user_service = UserService()  

    async def register_user(self, user_data: UserCreate, db: AsyncSession):
        """
        Registers a new user using RFID.

        Args:
            user_data (UserCreate): User data for registration.
            db (AsyncSession): Database session.

        Returns:
            JSONResponse: A standardized response with the newly created user.
        """
        user = await self.user_service.register_user(db, user_data)
        if not user:
            return AppResponse.send_error(
                message="RFID UID is already registered.",
                status_code=400
            )

        return AppResponse.send_success(
            data={"user_id": user.id, "rfid_uid": user.rfid_uid},
            message="User registered successfully."
        )

    async def authenticate_rfid(self, rfid_uid: str, db: AsyncSession):
        """
        Authenticates a user using RFID UID and generates tokens.

        Args:
            rfid_uid (str): RFID UID of the user.
            db (AsyncSession): Database session.

        Returns:
            JSONResponse: A standardized response with access and refresh tokens.
        """
        tokens = await self.user_service.authenticate_rfid(db, rfid_uid)
        if not tokens:
            return AppResponse.send_error(
                message="RFID not registered.",
                status_code=401
            )

        return AppResponse.send_success(
            data=tokens,
            message="User authenticated successfully."
        )
