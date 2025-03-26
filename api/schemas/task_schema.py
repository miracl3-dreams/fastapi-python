from pydantic import BaseModel, field_serializer
from typing import Optional

class TaskCreate(BaseModel):
    task_name: str
    task_description: Optional[str] = None  # ✅ Optional
    status: bool = False  # ✅ Default to False

class TaskUpdate(BaseModel):
    task_name: str
    task_description: Optional[str] = None  # ✅ Optional
    status: bool = False  # ✅ Default to False

class TaskDelete(BaseModel):
    id: int

class TaskResponse(BaseModel):
    id: int 
    task_name: str
    task_description: Optional[str] = None  # ✅ Optional
    status: bool
    
    @field_serializer("status")
    def format_status(self, status: bool) -> str:
        """Convert boolean status to 'completed' or 'incomplete'."""
        return "completed" if status else "incomplete"
    
    class Config:
        from_attributes = True
