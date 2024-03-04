from fastapi import APIRouter, Depends

from server.db.crud import AbstractTaskRepository, get_task_crud
from server.schemas.tasks import TaskCreate, TaskFilter, TaskRead, TaskUpdate

router_tasks = APIRouter(
    tags=["tasks"],
    prefix="/tasks",
)


@router_tasks.get("/")
async def get_tasks(
    offset: int = 0,
    limit: int = 100,
    filters: TaskFilter = Depends(),
    crud: AbstractTaskRepository = Depends(get_task_crud),
) -> list[TaskRead]:
    """Роут для получение списка задач"""
    result = await crud.get_tasks(filters=filters, offset=offset, limit=limit)
    return result


@router_tasks.get("/{task_id}")
async def get_task(
    task_id: int,
    crud: AbstractTaskRepository = Depends(get_task_crud),
) -> TaskRead:
    """Роут для получение задачи по id"""
    result = await crud.get_task(task_id=task_id)
    return result


@router_tasks.post("/")
async def add_tasks(
    tasks: list[TaskCreate],
    crud: AbstractTaskRepository = Depends(get_task_crud),
):
    """Роут для добавление задач"""
    await crud.add_tasks(tasks=tasks)


@router_tasks.patch("/{task_id}")
async def update_task(
    task_id: int,
    update_data: TaskUpdate,
    crud: AbstractTaskRepository = Depends(get_task_crud),
):
    """Роут для обновление задачи"""
    await crud.update_task(task_id=task_id, update_data=update_data)
