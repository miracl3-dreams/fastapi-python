from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.utils.database import get_db  
from api.models.user_model import User
from api.utils.token_manager import TokenManager  

router = APIRouter()

@router.post("/register")
async def register_rfid(rfid_uid: str, first_name: str, last_name: str, gender: str, db: AsyncSession = Depends(get_db)):
    """
    Register a new user with an RFID UID.
    """
    result = await db.execute(select(User).filter(User.rfid_uid == rfid_uid))
    existing_user = result.scalars().first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="RFID already registered")

    new_user = User(rfid_uid=rfid_uid, first_name=first_name, last_name=last_name, gender=gender)
    db.add(new_user)
    await db.commit()  
    return {"message": "RFID registered successfully", "user_id": new_user.id}

@router.post("/rfid-login")
async def rfid_login(rfid_uid: str, db: AsyncSession = Depends(get_db)):
    """
    Authenticate user using RFID and generate JWT tokens.
    """
    result = await db.execute(select(User).filter(User.rfid_uid == rfid_uid))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=401, detail="RFID not registered")

    access_token = TokenManager.generate_access_token({"sub": user.rfid_uid})
    refresh_token = TokenManager.generate_refresh_token({"sub": user.rfid_uid})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh")
async def refresh_token(refresh_token: str):
    """
    Refresh the access token using a valid refresh token.
    """
    try:
        # Validate the refresh token
        decoded_payload = TokenManager.validate_refresh_token(refresh_token)
        access_token = TokenManager.generate_access_token({"sub": decoded_payload["sub"]})
        return {"access_token": access_token}
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
