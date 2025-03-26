from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.attendance_service import AttendanceService
from api.schemas.attendance_schema import AttendanceCreate
from api.utils.database import get_db
from api.utils.handle_exception import handle_exception

class AttendanceController:
    def __init__(self):
        self.attendance_service = AttendanceService()

    async def log_attendance(self, attendance_data: AttendanceCreate, db: AsyncSession = Depends(get_db)):
        """Logs attendance for a user."""
        try:
            attendance = await self.attendance_service.log_attendance(db, attendance_data)
            if not attendance:
                raise HTTPException(status_code=404, detail="User not found. Please register first.")
            return attendance
        except Exception as e:
            return handle_exception(e)
