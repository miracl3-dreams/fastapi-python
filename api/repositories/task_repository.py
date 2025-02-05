from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.task_model import Task
from api.schemas.task_schema import TaskCreate, TaskResponse
from api.utils.custom_error import NotFoundError
from sqlalchemy.orm import selectinload

class TaskRepository:
    async def create_task(self, db: AsyncSession, task_data: TaskCreate) -> TaskResponse:
        """Create a new task and store it in the database."""
        task = Task(
            task_name=task_data.task_name,
            task_description=task_data.task_description,
            status=task_data.status
        )
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return TaskResponse.from_orm(task)

    async def get_task_by_id(self, db: AsyncSession, task_id: int) -> TaskResponse:
        """Fetch a task by its ID."""
        query = select(Task).filter(Task.id == task_id)
        result = await db.execute(query)
        task = result.scalar_one_or_none()
        if not task:
            raise NotFoundError(f"Task with ID {task_id} not found.")
        return TaskResponse.from_orm(task)

    async def get_all_tasks(self, db: AsyncSession) -> list[TaskResponse]:
        """Retrieve all tasks."""
        query = select(Task)
        result = await db.execute(query)
        tasks = result.scalars().all()
        return [TaskResponse.from_orm(task) for task in tasks]

    async def update_task(self, db: AsyncSession, task_id: int, task_data: TaskCreate) -> TaskResponse:
        """Update an existing task."""
        task = await self.get_task_by_id(db, task_id)
        task.task_name = task_data.task_name
        task.task_description = task_data.task_description
        task.status = task_data.status
        await db.commit()
        await db.refresh(task)
        return TaskResponse.from_orm(task)

    async def delete_task(self, db: AsyncSession, task_id: int) -> bool:
        """Delete a task by its ID."""
        task = await self.get_task_by_id(db, task_id)
        await db.delete(task)
        await db.commit()
        return True
