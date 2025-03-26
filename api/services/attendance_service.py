from sqlalchemy.ext.asyncio import AsyncSession
from api.repositories.user_repository import UserRepository
from api.repositories.attendance_repository import AttendanceRepository
from api.schemas.attendance_schema import AttendanceCreate
from fastapi import HTTPException

class AttendanceService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.attendance_repository = AttendanceRepository()

    async def log_attendance(self, db: AsyncSession, attendance_data: AttendanceCreate):
        """Log attendance for a user based on their UID."""
        user = await self.user_repository.get_user_by_uid(db, attendance_data.uid)
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found. Please register first.")
        
        return await self.attendance_repository.log_attendance(db, user.id)
