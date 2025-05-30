from sqlalchemy import Column, Integer, Text, String, Boolean
# from sqlalchemy.sql import func
from ..models import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task_name = Column(String(255), unique=True, nullable=False)
    task_description = Column(Text, nullable=True)  
    status = Column(Boolean, default=False, nullable=False)
    
    def status_label(self):
        """Returns 'incomplete' if False, 'complete' if True."""
        return "complete" if self.status else "incomplete"