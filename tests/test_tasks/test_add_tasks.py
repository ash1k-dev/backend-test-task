import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.db.models import Task
from tests.test_tasks.task_test_data import LIST_DATA_ADD_TASKS


@pytest.mark.parametrize(
    "tasks_data, tasks_len, tasks_status_code", LIST_DATA_ADD_TASKS
)
async def test_add_tasks(
    tasks_data: list[dict],
    tasks_len: int,
    tasks_status_code: int,
    ac: AsyncClient,
    session: AsyncSession,
):
    res = await ac.post("/tasks/", json=tasks_data)
    assert res.status_code == tasks_status_code
    statement = select(Task)
    result = await session.execute(statement)
    task_models = result.scalars().all()
    assert len(task_models) == tasks_len
