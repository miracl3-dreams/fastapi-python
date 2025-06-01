from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.utils.token_manager import TokenManager
from api.utils.database import get_db
from api.models.user_model import User  

auth_scheme = HTTPBearer()

async def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
    db: AsyncSession = Depends(get_db)
):
    token = credentials.credentials
    try:
        payload = TokenManager.validate_token(token)

        # Extract RFID UID from token payload (usually in "sub")
        rfid_uid = payload.get("sub")
        if not rfid_uid:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        # Query user by RFID UID
        query = select(User).filter(User.rfid_uid == rfid_uid)
        result = await db.execute(query)
        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        # Replace 'id' with actual user.id for downstream usage
        payload["id"] = user.id

        return payload

    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
