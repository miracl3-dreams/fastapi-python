from sqlalchemy.orm import Session
from api.models.attendance_model import Attendance

class AttendanceRepository:
    @staticmethod
    def log_attendance(db: Session, user_id: int):
        new_attendance = Attendance(user_id=user_id)
        db.add(new_attendance)
        db.commit()
        db.refresh(new_attendance)
        return new_attendance
