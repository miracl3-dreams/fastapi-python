from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.controllers.task_controller import TaskController
from api.schemas.task_schema import TaskCreate
from api.utils.database import AsyncSessionLocal

router = APIRouter()
task_controller = TaskController()

# Dependency to get the database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
        
@router.post("/create", response_model=TaskCreate)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_controller.create_task(task, db)