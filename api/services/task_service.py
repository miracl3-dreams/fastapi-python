from api.repositories.task_repository import TaskRepository
from api.schemas.task_schema import TaskCreate, TaskResponse
from sqlalchemy.ext.asyncio import AsyncSession
from api.utils.handle_exception import handle_exception

class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    async def create_task(self, task_data: TaskCreate, db: AsyncSession) -> TaskResponse:
        """Create a new task."""
        try:
            return await self.task_repository.create_task(db, task_data)
        except Exception as e:
            return handle_exception(e)

    async def get_task_by_id(self, task_id: int, db: AsyncSession) -> TaskResponse:
        """Get a task by its ID."""
        try:
            return await self.task_repository.get_task_by_id(db, task_id)
        except Exception as e:
            return handle_exception(e)

    async def get_all_tasks(self, db: AsyncSession) -> list[TaskResponse]:
        """Get all tasks."""
        try:
            return await self.task_repository.get_all_tasks(db)
        except Exception as e:
            return handle_exception(e)

    async def update_task(self, task_id: int, task_data: TaskCreate, db: AsyncSession) -> TaskResponse:
        """Update a task."""
        try:
            return await self.task_repository.update_task(db, task_id, task_data)
        except Exception as e:
            return handle_exception(e)

    async def delete_task(self, task_id: int, db: AsyncSession) -> bool:
        """Delete a task by its ID."""
        try:
            return await self.task_repository.delete_task(db, task_id)
        except Exception as e:
            return handle_exception(e)
        
    async def search_tasks(self, query: str, db: AsyncSession) -> list[TaskResponse]:
        """Search tasks by title, description, or other fields."""
        try:
            tasks = await self.task_repository.search_tasks(db, query)
            return tasks
        except Exception as e:
            return handle_exception(e)
