from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    rfid_uid: str
    first_name: str
    last_name: str
    gender: str

class UserResponse(BaseModel):
    id: int
    rfid_uid: str
    first_name: str
    last_name: str
    gender: str
    registered_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

