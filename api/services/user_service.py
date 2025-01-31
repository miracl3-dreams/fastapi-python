# services/user_service.py
from api.repositories.user_repository import create_user, get_user_by_email
from api.schemas.user_schema import UserCreate
from api.utils.encryption import hash_password, verify_password

async def create_new_user(db, user_data: UserCreate):
    hashed_password = hash_password(user_data.password)
    user_data.password = hashed_password
    return await create_user(db, user_data)

async def authenticate_user(db, email: str, password: str):
    user = get_user_by_email(db, email)
    if user and verify_password(password, user.password):  # Implement verify_password in encryption.py
        return user
    return None