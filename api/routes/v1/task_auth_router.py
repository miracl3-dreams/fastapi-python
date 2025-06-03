from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.controllers.task_controller import TaskController
from api.schemas.task_schema import TaskCreate, TaskUpdate, TaskDelete, TaskResponse
from api.utils.database import get_db
from api.middlewares.auth_guard import verify_token  

router = APIRouter()
task_controller = TaskController()

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return await task_controller.get_task(task_id, db, user)


@router.get("/", response_model=List[TaskResponse])
async def get_all_tasks(
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return await task_controller.get_all_tasks(db, user)


@router.post("/", response_model=TaskResponse)
async def create_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return await task_controller.create_task(task, db, user)


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return await task_controller.update_task(task_id, task, db, user)


@router.delete("/{task_id}", response_model=TaskDelete)
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return await task_controller.delete_task(task_id, db, user)


@router.get("/search", response_model=List[TaskResponse])
async def search_tasks(
    query: str,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(verify_token)
):
    return await task_controller.search_tasks(query, db, user)
