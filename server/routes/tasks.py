from fastapi import APIRouter, Depends

from server.db.crud import TaskRepository
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
) -> list[TaskRead]:
    """Получение списка задач"""
    result = await TaskRepository.get_tasks(filters=filters, offset=offset, limit=limit)
    return result


@router_tasks.get("/{task_id}")
async def get_task(task_id: int) -> TaskRead:
    """Получение задачи по id"""
    result = await TaskRepository.get_task(task_id=task_id)
    return result


@router_tasks.post("/")
async def add_tasks(
    tasks: list[TaskCreate],
):
    """Добавление задач"""
    await TaskRepository.add_tasks(tasks=tasks)


@router_tasks.patch("/{task_id}")
async def update_task(task_id: int, update_data: TaskUpdate):
    """Обновление задачи"""
    await TaskRepository.update_task(task_id=task_id, update_data=update_data)
