from sqlalchemy.ext.asyncio import AsyncSession
from api.models.attendance_model import Attendance

class AttendanceRepository:
    def __init__(self):
        pass  

    async def log_attendance(self, db: AsyncSession, user_id: int) -> Attendance:
        new_attendance = Attendance(user_id=user_id)
        db.add(new_attendance)
        await db.commit()
        await db.refresh(new_attendance)
        return new_attendance
