from pydantic import BaseModel, field_serializer
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    task_name: str
    task_description: Optional[str] = None
    status: bool = False

class TaskUpdate(BaseModel):
    task_name: str
    task_description: Optional[str] = None
    status: bool = False

class TaskDelete(BaseModel):
    id: int
    
class TaskResponse(BaseModel):
    id: int
    task_name: str
    task_description: Optional[str] = None 
    status: bool
    
    @field_serializer("status")
    async def format_status(self, status: bool) -> str:
        """Convert boolean status to 'completed' or 'incomplete'.""" 
        return "completed" if status else "incomplete"
    
    class Config:
        from_attributes = True


