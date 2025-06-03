from sqlalchemy.ext.asyncio import AsyncSession
from api.utils.app_response import AppResponse
from api.services.task_service import TaskService
from api.schemas.task_schema import TaskCreate
from api.utils.handle_exception import handle_exception

class TaskController:
    """
    Controller for handling task to create, get, update, delete, search.
    """
    
    def __init__(self):
        self.task_service = TaskService()

    async def create_task(self, task_data: TaskCreate, db: AsyncSession, user: dict):
        """Create a new task for the authenticated user."""
        try:
            task = await self.task_service.create_task(task_data, db, user["id"])
            return AppResponse.send_success(data=task.model_dump(), message="Task created successfully")
        except Exception as e:
            return handle_exception(e)

    async def get_task(self, task_id: int, db: AsyncSession, user: dict):
        """Retrieve a task by its ID, ensuring it belongs to the user."""
        try:
            task = await self.task_service.get_task_by_id(task_id, db, user["id"])
            return AppResponse.send_success(data=task.model_dump(), message="Task retrieved successfully")
        except Exception as e:
            return handle_exception(e)

    async def get_all_tasks(self, db: AsyncSession, user: dict):
        """Retrieve all tasks for the authenticated user."""
        try:
            tasks = await self.task_service.get_all_tasks(db, user["id"])
            return AppResponse.send_success(data=[t.model_dump() for t in tasks], message="All Tasks retrieved successfully")
        except Exception as e:
            return handle_exception(e)

    async def update_task(self, task_id: int, task_data: TaskCreate, db: AsyncSession, user: dict):
        """Update a task only if it belongs to the authenticated user."""
        try:
            task = await self.task_service.update_task(task_id, task_data, db, user["id"])
            return AppResponse.send_success(data=task.model_dump(), message="Task updated successfully")
        except Exception as e:
            return handle_exception(e)

    async def delete_task(self, task_id: int, db: AsyncSession, user: dict):
        """Delete a task only if it belongs to the authenticated user."""
        try:
            await self.task_service.delete_task(task_id, db, user["id"])
            return AppResponse.send_success(message="Task successfully deleted")
        except Exception as e:
            return handle_exception(e)

    async def search_tasks(self, query: str, db: AsyncSession, user: dict):
        """Search tasks by name or description within the user's tasks."""
        try:
            tasks = await self.task_service.search_tasks(query, db, user["id"])
            return AppResponse.send_success(data=[t.model_dump() for t in tasks], message="Tasks found successfully")
        except Exception as e:
            return handle_exception(e)
