from sqlalchemy import Column, Integer, String, Boolean
from api.utils.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  
    is_active = Column(Boolean, default=True)  