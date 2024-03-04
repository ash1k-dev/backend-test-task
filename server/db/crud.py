from abc import ABC, abstractmethod
from datetime import datetime

from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from server.db.database import get_db
from server.db.models import Product, Task
from server.schemas.products import ProductCreate
from server.schemas.tasks import TaskCreate, TaskFilter, TaskRead, TaskUpdate


def to_pydantic(db_object, pydantic_model):
    """Преобразование объекта базы данных в модель Pydantic"""
    return pydantic_model(**db_object.__dict__)


class AbstractTaskRepository(ABC):
    """Абстрактная реализация репозитория задач"""

    @abstractmethod
    async def add_tasks(self, tasks: list[TaskCreate]):
        """Создание задач"""
        pass

    @abstractmethod
    async def get_tasks(self, filters: TaskFilter, offset: int = 0, limit: int = 100):
        """Получение задач"""
        pass

    @abstractmethod
    async def get_task(self, task_id: int):
        """Получение задачи"""
        pass

    @abstractmethod
    async def update_task(self, task_id: int, update_data: TaskUpdate):
        """Обновление задачи"""
        pass


class TaskRepository(AbstractTaskRepository):
    """Класс для работы с задачами"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_tasks(self, tasks: list[TaskCreate]) -> None:
        """Создание задач"""
        for task in tasks:
            statement = select(Task).where(
                Task.task_number == task.task_number,
                Task.task_date == task.task_date,
            )
            result = await self.session.execute(statement)
            task_models = result.scalar_one_or_none()
            if task_models:
                await self.session.delete(task_models)
                await self.session.commit()
            self.session.add(Task(**task.model_dump()))
            await self.session.commit()

    async def get_tasks(
        self, filters: TaskFilter, offset: int = 0, limit: int = 100
    ) -> list[TaskRead]:
        """Получение задач"""
        statement = (
            select(Task)
            .filter_by(**filters.model_dump(exclude_none=True))
            .offset(offset)
            .limit(limit)
        )
        result = await self.session.execute(statement)
        task_models = result.scalars().all()
        tasks = [to_pydantic(task_model, TaskRead) for task_model in task_models]
        return tasks

    async def get_task(self, task_id: int) -> TaskRead:
        """Получение задачи"""
        statement = (
            select(Task)
            .where(Task.id == task_id)
            .options(selectinload(Task.products).load_only(Product.product_code))
        )
        result = await self.session.execute(statement)
        task_model = result.scalar_one_or_none()
        if task_model:
            return to_pydantic(task_model, TaskRead)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )

    async def update_task(self, task_id: int, update_data: TaskUpdate) -> None:
        """Обновление задачи"""
        statement = select(Task).where(Task.id == task_id)
        result = await self.session.execute(statement)
        task_model = result.scalar_one_or_none()
        if task_model:
            for field, value in update_data.dict(exclude_unset=True).items():
                setattr(task_model, field, value)
                if field == "task_status" and value:
                    task_model.closed_at = datetime.now() if value else None
            await self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )


class AbstractProductRepository(ABC):
    """Абстрактная реализация репозитория продуктов"""

    @abstractmethod
    async def create_products(self, products: list[ProductCreate]):
        """Создание продуктов"""
        pass

    @abstractmethod
    async def aggregate_product(self, task_number: int, product_code: str):
        """Агрегирование продукта"""
        pass


class ProductRepository(AbstractProductRepository):
    """Класс для работы с продуктами"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_products(self, products: list[ProductCreate]) -> None:
        """Создание продуктов"""
        statement = select(Task.task_number, Task.task_date)
        result = await self.session.execute(statement)
        task_models = result.all()
        statement = select(Product.product_code)
        result = await self.session.execute(statement)
        product_models = result.all()
        product_list = []
        for product in products:
            if (product.task_number, product.task_date) not in task_models or (
                (product.product_code,) in product_models
            ):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="there is no task number with this date or code are not unique",
                )
            product_list.append(Product(**product.model_dump()))
            self.session.add_all(product_list)
            await self.session.commit()

    async def aggregate_product(self, task_number: int, product_code: str):
        """Агрегирование продукта"""
        statement = select(Task).where(
            Task.task_number == task_number,
        )
        result = await self.session.execute(statement)
        task_models = result.scalar_one_or_none()
        if task_models.task_status:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="task is closed",
            )
        elif task_models:
            statement = select(Product).where(
                Product.product_code == product_code,
                Product.task_number == task_number,
            )
            result = await self.session.execute(statement)
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
                    await self.session.commit()
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="unique code is attached to another batch",
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )


async def get_task_crud(db: AsyncSession = Depends(get_db)):
    """Функция для получения репозитория задач"""
    return TaskRepository(session=db)


async def get_product_crud(db: AsyncSession = Depends(get_db)):
    """Функция для получения репозитория продуктов"""
    return ProductRepository(session=db)
