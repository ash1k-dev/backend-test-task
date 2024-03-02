from fastapi import APIRouter


router_tasks = APIRouter(
    tags=["tasks"],
    prefix="/tasks",
)


@router_tasks.get("/")
async def get_tasks():
    pass


@router_tasks.get("/{task_id}")
async def get_task(task_id):
    pass


@router_tasks.post("/")
async def add_tasks(
    tasks,
):
    pass


@router_tasks.patch("/{task_id}")
async def update_task(task_id, update_data):
    pass
