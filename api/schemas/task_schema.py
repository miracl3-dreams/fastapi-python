from pydantic import BaseModel

class TaskCreate(BaseModel):
    task_name: str
    task_description: str
    status: bool

class TaskResponse(BaseModel):
    id: int 
    task_name: str
    task_description: str
    status: bool
    
    class Config:
        from_attributes = True
    