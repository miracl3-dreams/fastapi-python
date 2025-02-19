from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.task_service import TaskService
from api.schemas.task_schema import TaskCreate, TaskResponse
from api.utils.custom_error import AuthError
from api.utils.handle_exception import handle_exception

class TaskController:
    def __init__(self):
        self.task_service = TaskService()

    async def create_task(self, task_data: TaskCreate, db: AsyncSession) -> TaskResponse:
        """Create a new task."""
        try:
            task = await self.task_service.create_task(task_data, db)
            return task
        except AuthError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            return handle_exception(e)

    async def get_task(self, task_id: int, db: AsyncSession) -> TaskResponse:
        """Retrieve a task by its ID."""
        try:
            task = await self.task_service.get_task_by_id(task_id, db)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            return task
        except Exception as e:
            return handle_exception(e)

    async def get_all_tasks(self, db: AsyncSession):
        """Retrieve all tasks."""
        try:
            tasks = await self.task_service.get_all_tasks(db)
            return tasks
        except Exception as e:
            return handle_exception(e)

    async def update_task(self, task_id: int, task_data: TaskCreate, db: AsyncSession):
        """Update a task by its ID."""
        try:
            task = await self.task_service.update_task(task_id, task_data, db)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            return task
        except Exception as e:
            return handle_exception(e)

    async def delete_task(self, task_id: int, db: AsyncSession):
        """Delete a task by its ID."""
        try:
            is_deleted = await self.task_service.delete_task(task_id, db)
            if not is_deleted:
                raise HTTPException(status_code=404, detail="Task not found")
            return {"message": "Task successfully deleted"}
        except Exception as e:
            return handle_exception(e)
