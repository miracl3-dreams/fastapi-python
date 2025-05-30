from sqlalchemy.orm import declarative_base

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Import all models to ensure they are registered with SQLAlchemy's metadata
from api.models.user_model import User
from api.models.task_model import Task
from api.tests.test_model import Test  
