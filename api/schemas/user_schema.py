from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    uid: str
    first_name: str
    last_name: str
    gender: str

class UserResponse(BaseModel):
    id: int
    uid: str
    first_name: str
    last_name: str
    gender: str
    registered_at: datetime
    is_active: bool

    class Config:
        from_attributes = True
