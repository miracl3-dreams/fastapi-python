from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.task_model import Task
from api.schemas.task_schema import TaskCreate

class TaskRepository:
    """
    Repository for handling database operations related to Task.
    """

    async def create_task(self, db: AsyncSession, task_data: TaskCreate, user_id: int) -> Task:
        """Create a new task for a user after ensuring the task name is unique per user."""
        query = select(Task).filter(Task.task_name == task_data.task_name, Task.user_id == user_id)
        result = await db.execute(query)
        if result.scalars().first():
            return None  

        task = Task(
            task_name=task_data.task_name,
            task_description=task_data.task_description,
            status=task_data.status,
            user_id=user_id
        )
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task

    async def get_task_by_id(self, db: AsyncSession, task_id: int, user_id: int) -> Task | None:
        """Retrieve a task by its ID for a specific user."""
        query = select(Task).filter(Task.id == task_id, Task.user_id == user_id)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def get_all_tasks(self, db: AsyncSession, user_id: int) -> list[Task]:
        """Retrieve all tasks for a specific user."""
        query = select(Task).filter(Task.user_id == user_id)
        result = await db.execute(query)
        return result.scalars().all()

    async def update_task(self, db: AsyncSession, task_id: int, task_data: TaskCreate, user_id: int) -> Task | None:
        """Update an existing task for a user."""
        task = await self.get_task_by_id(db, task_id, user_id)
        if not task:
            return None

        query = select(Task).filter(
            Task.task_name == task_data.task_name,
            Task.user_id == user_id,
            Task.id != task_id
        )
        result = await db.execute(query)
        if result.scalars().first():
            return False  

        task.task_name = task_data.task_name
        task.task_description = task_data.task_description
        task.status = task_data.status
        await db.commit()
        await db.refresh(task)
        return task

    async def delete_task(self, db: AsyncSession, task_id: int, user_id: int) -> bool:
        """Delete a task belonging to a user."""
        task = await self.get_task_by_id(db, task_id, user_id)
        if not task:
            return False
        await db.delete(task)
        await db.commit()
        return True
    
    async def search_tasks(self, db: AsyncSession, query: str, user_id: int) -> list[Task]:
        """Search tasks by name or description within a user's tasks."""
        stmt = select(Task).filter(
            (Task.task_name.ilike(f"%{query}%")) | (Task.task_description.ilike(f"%{query}%")),
            Task.user_id == user_id
        )
        result = await db.execute(stmt)
        return result.scalars().all()
