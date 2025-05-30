from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.user_model import User

class UserRepository:
    @staticmethod
    async def get_user_by_rfid(db: AsyncSession, rfid_uid: str):
        """Fetch a user by RFID UID."""
        result = await db.execute(select(User).filter(User.rfid_uid == rfid_uid))
        return result.scalars().first()

    @staticmethod
    async def create_user(db: AsyncSession, rfid_uid: str, first_name: str, last_name: str, gender: str):
        """Create a new user in the database."""
        new_user = User(rfid_uid=rfid_uid, first_name=first_name, last_name=last_name, gender=gender)
        db.add(new_user)

        await db.commit()  
        await db.refresh(new_user)  

        return new_user
