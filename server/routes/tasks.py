from fastapi import APIRouter
from pydantic import ValidationError

from server.schemas.tasks import TaskCreate, TaskRead, TaskUpdate
from server.db.crud import TaskRepository

router_tasks = APIRouter(
    tags=["tasks"],
    prefix="/tasks",
)


@router_tasks.get("/")
async def get_tasks() -> list[TaskRead]:
    try:
        result = await TaskRepository.get_tasks()
        return result
    except ValidationError as e:
        print(e.json())


@router_tasks.get("/{task_id}")
async def get_task(task_id: int):
    result = await TaskRepository.get_task(task_id=task_id)
    return result


@router_tasks.post("/")
async def add_tasks(
    tasks: list[TaskCreate],
):
    await TaskRepository.add_tasks(tasks=tasks)


@router_tasks.patch("/{task_id}")
async def update_task(task_id: int, update_data: TaskUpdate):
    await TaskRepository.update_task(task_id=task_id, update_data=update_data)
