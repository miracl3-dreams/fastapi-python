from sqlalchemy.orm import Session
from api.repositories.user_repository import UserRepository
from api.repositories.attendance_repository import AttendanceRepository
from api.schemas.attendance_schema import AttendanceCreate

class AttendanceService:
    @staticmethod
    def log_attendance(db: Session, attendance_data: AttendanceCreate):
        user = UserRepository.get_user_by_uid(db, attendance_data.uid)
        if not user:
            return None  
        return AttendanceRepository.log_attendance(db, user.id)
