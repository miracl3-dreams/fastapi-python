from pydantic import BaseModel
from datetime import datetime

class AttendanceCreate(BaseModel):
    uid: str  

class AttendanceResponse(BaseModel):
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True
