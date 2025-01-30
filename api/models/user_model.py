from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from api.models.role_model import Role
from api.models.gender_model import Gender

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role] = []  
    
class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
