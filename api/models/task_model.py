from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..models import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task_name = Column(String(255), unique=True, nullable=False)
    task_description = Column(Text, nullable=True)
    status = Column(Boolean, default=False, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user = relationship("User", back_populates="tasks")

    def status_label(self):
        return "complete" if self.status else "incomplete"
