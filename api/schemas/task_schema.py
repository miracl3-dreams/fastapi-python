from pydantic import BaseModel, field_serializer, ConfigDict
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    task_name: str
    task_description: Optional[str] = None
    status: bool = False

class TaskUpdate(BaseModel):
    task_name: Optional[str] = None
    task_description: Optional[str] = None
    status: Optional[bool] = None

class TaskDelete(BaseModel):
    id: int
    
class TaskResponse(BaseModel):
    id: int
    task_name: str
    task_description: Optional[str] = None 
    status: bool
    
    @field_serializer("status")
    def serialize_status(self, status: bool, _info) -> str:
        return "completed" if status else "incomplete"

    model_config = ConfigDict(from_attributes=True)



