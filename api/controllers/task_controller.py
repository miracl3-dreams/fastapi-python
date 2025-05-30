from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.services.task_service import TaskService
from api.schemas.task_schema import TaskCreate, TaskResponse
from api.utils.custom_error import AuthError
from api.utils.handle_exception import handle_exception

class TaskController:
    def __init__(self):
        self.task_service = TaskService()

    async def create_task(self, task_data: TaskCreate, db: AsyncSession, user: dict) -> TaskResponse:
        """Create a new task for the authenticated user."""
        try:
            return await self.task_service.create_task(task_data, db, user["id"])
        except AuthError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            return handle_exception(e)

    async def get_task(self, task_id: int, db: AsyncSession, user: dict) -> TaskResponse:
        """Retrieve a task by its ID, ensuring it belongs to the user."""
        try:
            task = await self.task_service.get_task_by_id(task_id, db, user["id"])
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            return task
        except Exception as e:
            return handle_exception(e)

    async def get_all_tasks(self, db: AsyncSession, user: dict):
        """Retrieve all tasks for the authenticated user."""
        try:
            return await self.task_service.get_all_tasks(db, user["id"])
        except Exception as e:
            return handle_exception(e)

    async def update_task(self, task_id: int, task_data: TaskCreate, db: AsyncSession, user: dict):
        """Update a task only if it belongs to the authenticated user."""
        try:
            task = await self.task_service.update_task(task_id, task_data, db, user["id"])
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            return task
        except Exception as e:
            return handle_exception(e)

    async def delete_task(self, task_id: int, db: AsyncSession, user: dict):
        """Delete a task only if it belongs to the authenticated user."""
        try:
            is_deleted = await self.task_service.delete_task(task_id, db, user["id"])
            if not is_deleted:
                raise HTTPException(status_code=404, detail="Task not found")
            return {"message": "Task successfully deleted"}
        except Exception as e:
            return handle_exception(e)

    async def search_tasks(self, query: str, db: AsyncSession, user: dict) -> list[TaskResponse]:
        """Search tasks by name or description within the user's tasks."""
        try:
            tasks = await self.task_service.search_tasks(query, db, user["id"])
            if not tasks:
                raise HTTPException(status_code=404, detail="No tasks found matching the query")
            return tasks
        except Exception as e:
            return handle_exception(e)
