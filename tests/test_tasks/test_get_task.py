import pytest
from db.models import Task
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tests.test_tasks.task_test_data import LIST_DATA_GET_TASK_ID


@pytest.mark.parametrize(
    "tasks_data,task_number, task_id_status_code", LIST_DATA_GET_TASK_ID
)
async def test_get_task(
    tasks_data: list[dict],
    task_number: int,
    task_id_status_code: int,
    ac: AsyncClient,
    session: AsyncSession,
):
    """Тест получения задачи"""
    await ac.post("/tasks/", json=tasks_data)
    statement = select(Task).where(Task.task_number == task_number)
    res = await session.execute(statement)
    res = res.scalars().first()
    res = await ac.get(f"/tasks/{res.id}")
    assert res.status_code == task_id_status_code
