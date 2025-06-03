from fastapi import HTTPException
from api.repositories.task_repository import TaskRepository
from api.schemas.task_schema import TaskCreate, TaskResponse
from sqlalchemy.ext.asyncio import AsyncSession

class TaskService:
    """
    Service layer for handling business logic related to Creating, Updating, Getting, Deleting Tasks.
    """
    
    def __init__(self):
        self.task_repository = TaskRepository()

    async def create_task(self, task_data: TaskCreate, db: AsyncSession, user_id: int) -> TaskResponse:
        """Create a new task for the authenticated user."""
        task = await self.task_repository.create_task(db, task_data, user_id)
        return TaskResponse.model_validate(task)


    async def get_task_by_id(self, task_id: int, db: AsyncSession, user_id: int) -> TaskResponse:
        """Get a task by ID only if it belongs to the user."""
        task = await self.task_repository.get_task_by_id(db, task_id, user_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return TaskResponse.model_validate(task)

    async def get_all_tasks(self, db: AsyncSession, user_id: int) -> list[TaskResponse]:
        """Get all tasks belonging to the authenticated user."""
        tasks = await self.task_repository.get_all_tasks(db, user_id)
        return [TaskResponse.model_validate(task) for task in tasks]

    async def update_task(self, task_id: int, task_data: TaskCreate, db: AsyncSession, user_id: int) -> TaskResponse:
        """Update a task only if it belongs to the user."""
        updated_task = await self.task_repository.update_task(db, task_id, task_data, user_id)
        if updated_task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        if updated_task is False:
            raise HTTPException(status_code=400, detail="Task name already exists.")
        return TaskResponse.model_validate(updated_task)
    
    async def delete_task(self, task_id: int, db: AsyncSession, user_id: int) -> bool:
        """Delete a task only if it belongs to the user."""
        is_deleted = await self.task_repository.delete_task(db, task_id, user_id)
        if not is_deleted:
            raise HTTPException(status_code=404, detail="Task not found")
        return True

    async def search_tasks(self, query: str, db: AsyncSession, user_id: int) -> list[TaskResponse]:
        """Search tasks by name or description within the user's tasks."""
        tasks = await self.task_repository.search_tasks(db, query, user_id)
        return [TaskResponse.model_validate(task) for task in tasks]
