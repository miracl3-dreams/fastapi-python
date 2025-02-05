# # services/user_service.py
# from api.repositories.user_repository import create_user, get_user_by_email
# from api.schemas.user_schema import UserCreate
# from api.utils.encryption import hash_password, verify_password

# async def create_new_user(db, user_data: UserCreate):
#     hashed_password = hash_password(user_data.password)
#     user_data.password = hashed_password
#     return await create_user(db, user_data)

# async def authenticate_user(db, email: str, password: str):
#     user = get_user_by_email(db, email)
#     if user and verify_password(password, user.password):  # Implement verify_password in encryption.py
#         return user
#     return None

from api.repositories.user_repository import UserRepository
from api.schemas.user_schema import UserCreate
from api.utils.encryption import hash_password, verify_password
from api.utils.custom_error import AuthError
from sqlalchemy.ext.asyncio import AsyncSession

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_new_user(self, db: AsyncSession, user_data: UserCreate):
        hashed_password = hash_password(user_data.password)
        user_data.password = hashed_password
        # Call the repository to store the new user
        return await self.user_repository.create_user(db, user_data)

    async def authenticate_user(self, db: AsyncSession, email: str, password: str):
        user = await self.user_repository.get_user_by_email(db, email)
        if user and verify_password(password, user.password):
            return user
        raise AuthError("Invalid credentials")
