from abc import ABC, abstractmethod
from datetime import datetime

from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.db.database import get_db
from server.db.models import Product, Task
from server.schemas.products import ProductCreate


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


async def get_product_crud(db: AsyncSession = Depends(get_db)):
    """Функция для получения репозитория продуктов"""
    return ProductRepository(session=db)
