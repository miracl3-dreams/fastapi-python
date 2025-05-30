from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from api.repositories.user_repository import UserRepository  
from api.utils.token_manager import TokenManager
from api.schemas.user_schema import UserCreate

class UserService:
    """
    Service layer for handling business logic related to user authentication and registration.
    """

    def __init__(self):
        self.token_manager = TokenManager()

    async def register_user(self, db: AsyncSession, user_data: UserCreate):
        """
        Registers a new user using RFID.
        
        Args:
            db (AsyncSession): Database session.
            user_data (UserCreate): User data for registration.

        Returns:
            User: The newly created user.
        """
        existing_user = await UserRepository.get_user_by_rfid(db, user_data.rfid_uid)  # ✅ Corrected
        if existing_user:
            raise HTTPException(status_code=400, detail="RFID UID is already registered.")

        new_user = await UserRepository.create_user(db, user_data.rfid_uid, user_data.first_name, user_data.last_name, user_data.gender)  # ✅ Corrected
        return new_user

    async def authenticate_rfid(self, db: AsyncSession, rfid_uid: str):
        """
        Authenticates a user using RFID and generates access and refresh tokens.

        Args:
            db (AsyncSession): Database session.
            rfid_uid (str): RFID UID of the user.

        Returns:
            dict: Access and refresh tokens.
        """
        user = await UserRepository.get_user_by_rfid(db, rfid_uid)  # ✅ Corrected
        if not user:
            raise HTTPException(status_code=401, detail="RFID not registered")

        access_token = self.token_manager.generate_access_token({"sub": user.rfid_uid})
        refresh_token = self.token_manager.generate_refresh_token({"sub": user.rfid_uid})

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

    async def refresh_token(self, refresh_token: str):
        """
        Refreshes the access token using a valid refresh token.

        Args:
            refresh_token (str): Refresh token.

        Returns:
            dict: New access token.
        """
        try:
            decoded_payload = self.token_manager.validate_refresh_token(refresh_token)
            access_token = self.token_manager.generate_access_token({"sub": decoded_payload["sub"]})
            return {"access_token": access_token}
        except ValueError:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
