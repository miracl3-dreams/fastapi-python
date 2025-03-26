from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from api.services.attendance_service import AttendanceService
from api.schemas.attendance_schema import AttendanceCreate, AttendanceResponse
from api.utils.database import get_db

class AttendanceController:
    @staticmethod
    def log_attendance(attendance_data: AttendanceCreate, db: Session = Depends(get_db)):
        attendance = AttendanceService.log_attendance(db, attendance_data)
        if not attendance:
            raise HTTPException(status_code=404, detail="User not found. Please register first.")
        return attendance
