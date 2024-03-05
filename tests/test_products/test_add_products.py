import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.db.models import Product
from tests.test_products.products_test_data import LIST_DATA_PRODUCTS_TASKS


@pytest.mark.parametrize(
    "tasks_data,products_data, products_len, products_status_code",
    LIST_DATA_PRODUCTS_TASKS,
)
async def test_add_products(
    tasks_data: list[dict],
    products_data: list[dict],
    products_len: int,
    products_status_code: int,
    ac: AsyncClient,
    session: AsyncSession,
):
    """Тест добавления продуктов"""
    await ac.post("/tasks/", json=tasks_data)
    res = await ac.post("/products/", json=products_data)
    assert res.status_code == products_status_code
    statement = select(Product)
    result = await session.execute(statement)
    task_models = result.scalars().all()
    assert len(task_models) == products_len
