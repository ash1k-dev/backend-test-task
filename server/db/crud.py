from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from server.db.database import async_session_maker
from server.db.models import Product, Task
from server.schemas.products import ProductCreate
from server.schemas.tasks import TaskCreate, TaskRead, TaskUpdate


def to_pydantic(db_object, pydantic_model):
    """Преобразование объекта базы данных в модель Pydantic"""
    return pydantic_model(**db_object.__dict__)


class TaskRepository:
    """Класс для работы с задачами"""

    @classmethod
    async def add_tasks(cls, tasks: list[TaskCreate]) -> None:
        """Создание задач"""
        async with async_session_maker() as session:
            for task in tasks:
                statement = select(Task).where(
                    Task.task_number == task.task_number,
                    Task.task_date == task.task_date,
                )
                result = await session.execute(statement)
                task_models = result.scalar_one_or_none()
                if task_models:
                    await session.delete(task_models)
                    await session.commit()
                session.add(Task(**task.model_dump()))
                await session.commit()

    @classmethod
    async def get_tasks(cls) -> list[TaskRead]:
        """Получение задач"""
        async with async_session_maker() as session:
            statement = select(Task)
            result = await session.execute(statement)
            task_models = result.scalars().all()
            tasks = [to_pydantic(task_model, TaskRead) for task_model in task_models]
            return tasks

    @classmethod
    async def get_task(cls, task_id: int) -> TaskRead:
        """Получение задачи"""
        async with async_session_maker() as session:
            statement = (
                select(Task)
                .where(Task.id == task_id)
                .options(selectinload(Task.products).load_only(Product.product_code))
            )
            result = await session.execute(statement)
            task_model = result.scalar_one_or_none()
            if task_model:
                return to_pydantic(task_model, TaskRead)
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
                )

    @classmethod
    async def update_task(cls, task_id: int, update_data: TaskUpdate) -> None:
        """Обновление задачи"""
        async with async_session_maker() as session:
            statement = select(Task).where(Task.id == task_id)
            result = await session.execute(statement)
            task_model = result.scalar_one_or_none()
            if task_model:
                for field, value in update_data.dict(exclude_unset=True).items():
                    setattr(task_model, field, value)
                    if field == "task_status" and value:
                        task_model.closed_at = datetime.now() if value else None
                await session.commit()
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
                )


class ProductRepository:
    """Класс для работы с продуктами"""

    @classmethod
    async def create_products(cls, products: list[ProductCreate]) -> None:
        """Создание продуктов"""
        async with async_session_maker() as session:
            statement = select(Task.task_number, Task.task_date)
            result = await session.execute(statement)
            task_models = result.all()
            statement = select(Product.product_code)
            result = await session.execute(statement)
            product_models = result.all()
            product_list = []
            for product in products:
                if (
                    product.task_number,
                    product.task_date,
                ) not in task_models or ((product.product_code,) in product_models):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="there is no task number with this date or code are not unique",
                    )
                product_list.append(Product(**product.model_dump()))
            session.add_all(product_list)
            await session.commit()

    @classmethod
    async def aggregate_product(cls, task_number: int, product_code: str):
        """Агрегирование продукта"""
        async with async_session_maker() as session:
            statement = select(Task).where(
                Task.task_number == task_number,
            )
            result = await session.execute(statement)
            task_models = result.scalar_one_or_none()
            if task_models:
                statement = select(Product).where(
                    Product.product_code == product_code,
                    Product.task_number == task_number,
                )
                result = await session.execute(statement)
                product_models = result.scalar_one_or_none()
                if product_models:
                    if product_models.is_aggregated:
                        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"unique code already used at {product_models.aggregated_at}",
                        )
                    else:
                        product_models.is_aggregated = True
                        product_models.aggregated_at = datetime.now()
                        await session.commit()
                else:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="unique code is attached to another batch",
                    )
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
                )
