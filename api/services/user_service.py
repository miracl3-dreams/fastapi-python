from api.repositories.user_repository import UserRepository
from api.schemas.user_schema import UserCreate
from api.utils.encryption import hash_password, verify_password
from api.utils.custom_error import AuthError
from sqlalchemy.ext.asyncio import AsyncSession
from api.utils.exceptions import EmailAlreadyExistsException

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_new_user(self, db: AsyncSession, user_data: UserCreate):
        hashed_password = hash_password(user_data.password)
        user_data.password = hashed_password
        
        try:
            user = await self.user_repository.create_user(db, user_data)
        except EmailAlreadyExistsException as e:
            raise EmailAlreadyExistsException()  
        return user  
        

    async def authenticate_user(self, db: AsyncSession, email: str, password: str):
        user = await self.user_repository.get_user_by_email(db, email)
        if user and verify_password(password, user.password):
            return user
        raise AuthError()
