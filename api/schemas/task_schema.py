from pydantic import BaseModel

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
    
    class Config:
        from_attributes = True
    