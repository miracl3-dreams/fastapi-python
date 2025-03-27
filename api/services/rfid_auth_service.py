from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.user_model import User  
from api.utils.token_manager import TokenManager

class RFIDAuthService:
    """
    Service to authenticate users using RFID cards.
    """

    async def authenticate_rfid(self, uid: str, db: AsyncSession) -> dict:
        """
        Authenticate user using RFID UID.

        Args:
            uid (str): RFID UID (unique identifier).
            db (AsyncSession): Database session.

        Returns:
            dict: Authentication response with token or error message.
        """
        async with db as session:
            result = await session.execute(select(User).where(User.uid == uid))
            user = result.scalars().first()

            if not user:
                return {"error": "RFID UID not recognized."}

            # Generate JWT Token
            token = TokenManager.generate_access_token(
                {"user_id": user.id, "first_name": user.first_name, "last_name": user.last_name}
            )

            return {
                "message": "RFID authentication successful.",
                "access_token": token,
                "user": {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "gender": user.gender,
                    "registered_at": user.registered_at.isoformat(),
                    "is_active": user.is_active
                }
            }
