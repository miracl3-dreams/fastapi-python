from pydantic import BaseModel, Field, EmailStr

class AdminCreate(BaseModel): 
    email: EmailStr = Field(..., min_length=3, max_length=50, example="test123@gmail.com")
    password: str = Field(..., min_length=8, max_length=50, example="test1234")

class AdminResponse(BaseModel):
    id: int 
    email: EmailStr = Field(..., min_length=3, max_length=50, example="test123@gmail.com")

    class Config:
        from_attributes = True
