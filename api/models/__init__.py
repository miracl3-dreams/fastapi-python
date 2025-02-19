from sqlalchemy.ext.declarative import declarative_base

# Shared Base for all models
Base = declarative_base()

# Import all models to include them in Base.metadata
# This ensures Alembic autogenerate works across all models


from api.models.user_model import User
from api.models.admin_model import Admin
from api.models.task_model import Task
