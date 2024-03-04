import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from tests.test_tasks.task_test_data import LIST_DATA_GET_TASKS


@pytest.mark.parametrize(
    "tasks_data, tasks_len, tasks_status_code", LIST_DATA_GET_TASKS
)
async def test_get_tasks(
    tasks_data: list[dict],
    tasks_len: int,
    tasks_status_code: int,
    ac: AsyncClient,
    session: AsyncSession,
):
    """Тест получения задач"""
    await ac.post("/tasks/", json=tasks_data)
    res = await ac.get("/tasks/")
    assert res.status_code == tasks_status_code
    assert len(res.json()) == tasks_len
