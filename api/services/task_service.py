from api.repositories.task_repository import TaskRepository
from api.schemas.task_schema import TaskCreate, TaskResponse
from sqlalchemy.ext.asyncio import AsyncSession
from api.utils.handle_exception import handle_exception

class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    async def create_task(self, task_data: TaskCreate, db: AsyncSession, user_id: int) -> TaskResponse:
        """Create a new task for the authenticated user."""
        try:
            return await self.task_repository.create_task(db, task_data, user_id)
        except Exception as e:
            return handle_exception(e)

    async def get_task_by_id(self, task_id: int, db: AsyncSession, user_id: int) -> TaskResponse:
        """Get a task by ID only if it belongs to the user."""
        try:
            return await self.task_repository.get_task_by_id(db, task_id, user_id)
        except Exception as e:
            return handle_exception(e)

    async def get_all_tasks(self, db: AsyncSession, user_id: int) -> list[TaskResponse]:
        """Get all tasks belonging to the authenticated user."""
        try:
            return await self.task_repository.get_all_tasks(db, user_id)
        except Exception as e:
            return handle_exception(e)

    async def update_task(self, task_id: int, task_data: TaskCreate, db: AsyncSession, user_id: int) -> TaskResponse:
        """Update a task only if it belongs to the user."""
        try:
            return await self.task_repository.update_task(db, task_id, task_data, user_id)
        except Exception as e:
            return handle_exception(e)

    async def delete_task(self, task_id: int, db: AsyncSession, user_id: int) -> bool:
        """Delete a task only if it belongs to the user."""
        try:
            return await self.task_repository.delete_task(db, task_id, user_id)
        except Exception as e:
            return handle_exception(e)

    async def search_tasks(self, query: str, db: AsyncSession, user_id: int) -> list[TaskResponse]:
        """Search tasks by name or description within the user's tasks."""
        try:
            return await self.task_repository.search_tasks(db, query, user_id)
        except Exception as e:
            return handle_exception(e)
