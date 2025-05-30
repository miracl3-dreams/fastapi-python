from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models.task_model import Task
from api.schemas.task_schema import TaskCreate, TaskResponse
from api.utils.custom_error import NotFoundError
from fastapi import HTTPException

class TaskRepository:
    async def create_task(self, db: AsyncSession, task_data: TaskCreate, user_id: int):
        query = select(Task).filter(Task.task_name == task_data.task_name, Task.user_id == user_id)
        result = await db.execute(query)
        if result.scalars().first():
            raise HTTPException(status_code=400, detail="Task name already exists.")

        task = Task(
            task_name=task_data.task_name,
            task_description=task_data.task_description,
            status=task_data.status,
            user_id=user_id
        )
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return TaskResponse.model_validate(task)

    async def get_task_by_id(self, db: AsyncSession, task_id: int, user_id: int):
        query = select(Task).filter(Task.id == task_id, Task.user_id == user_id)
        result = await db.execute(query)
        task = result.scalar_one_or_none()
        if not task:
            raise NotFoundError(f"Task with ID {task_id} not found.")
        return TaskResponse.model_validate(task)

    async def get_all_tasks(self, db: AsyncSession, user_id: int) -> list[TaskResponse]:
        query = select(Task).filter(Task.user_id == user_id)
        result = await db.execute(query)
        tasks = result.scalars().all()
        return [TaskResponse.model_validate(task) for task in tasks]

    async def update_task(self, db: AsyncSession, task_id: int, task_data: TaskCreate, user_id: int):
        task = await self.get_task_by_id(db, task_id, user_id)
        task.task_name = task_data.task_name
        task.task_description = task_data.task_description
        task.status = task_data.status
        await db.commit()
        await db.refresh(task)
        return TaskResponse.model_validate(task)

    async def delete_task(self, db: AsyncSession, task_id: int, user_id: int) -> bool:
        task = await self.get_task_by_id(db, task_id, user_id)
        await db.delete(task)
        await db.commit()
        return True
    
    async def search_tasks(self, db: AsyncSession, query: str, user_id: int) -> list[TaskResponse]:
        stmt = select(Task).filter(
            (Task.task_name.ilike(f"%{query}%")) | (Task.task_description.ilike(f"%{query}%")),
            Task.user_id == user_id
        )
        result = await db.execute(stmt)
        tasks = result.scalars().all()
        return [TaskResponse.model_validate(task) for task in tasks]
