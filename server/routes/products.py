from typing import List

from fastapi import APIRouter, Depends

from server.db.crud import AbstractProductRepository, get_product_crud
from server.schemas.products import ProductCreate

router_products = APIRouter(
    tags=["products"],
    prefix="/products",
)


@router_products.post(
    "/",
)
async def add_products(
    products: List[ProductCreate],
    crud: AbstractProductRepository = Depends(get_product_crud),
):
    """Роут для добавления продуктов в базу данных"""
    await crud.create_products(products=products)


@router_products.get("/aggregate")
async def get_aggregate(
    task_number: int,
    product_code: str,
    crud: AbstractProductRepository = Depends(get_product_crud),
):
    """Роут для получения агрегированных данных по заданию и продукту"""
    result = await crud.aggregate_product(
        task_number=task_number, product_code=product_code
    )
    return result
