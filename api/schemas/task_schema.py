from pydantic import BaseModel, field_serializer

class TaskCreate(BaseModel):
    task_name: str
    task_description: str
    status: bool

class TaskUpdate(BaseModel):
    task_name: str
    task_description: str
    status: bool

class TaskDelete(BaseModel):
    id: int

class TaskResponse(BaseModel):
    id: int 
    task_name: str
    task_description: str
    status: bool
    
    @field_serializer("status")
    def format_status(self, status: bool) -> str:
        """Convert boolean status to 'completed' or 'incomplete'."""
        return "completed" if status else "incomplete"
    
    class Config:
        from_attributes = True