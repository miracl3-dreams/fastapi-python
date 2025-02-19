from sqlalchemy import Column, Integer, String
from api.utils.database import Base

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  