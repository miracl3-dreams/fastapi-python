from pydantic import BaseModel, ConfigDict

class AdminCreate(BaseModel):
    username: str
    password: str

class AdminResponse(BaseModel):
    id: int
    username: str

    class Config:
        model_config = ConfigDict(from_attributes=True)