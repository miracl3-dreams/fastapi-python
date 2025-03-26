from sqlalchemy.ext.asyncio import AsyncSession
from api.repositories.user_repository import UserRepository
from api.schemas.user_schema import UserCreate, UserResponse

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()  

    async def register_user(self, db: AsyncSession, user_data: UserCreate) -> UserResponse:
        """Register a new user."""
        existing_user = await self.user_repository.get_user_by_uid(db, user_data.uid)  

        if existing_user:
            raise Exception("User already exists")  

        new_user = await self.user_repository.create_user(db, user_data)
        return UserResponse.model_validate(new_user)
