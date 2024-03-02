from typing import List

from fastapi import APIRouter

from server.db.crud import ProductRepository
from server.schemas.products import ProductCreate

router_products = APIRouter(
    tags=["products"],
    prefix="/products",
)


@router_products.post(
    "/",
)
async def get_products(products: List[ProductCreate]):
    await ProductRepository.create_products(products=products)


@router_products.get("/aggregate")
async def get_aggregate(task_number: int, product_code: str):
    result = await ProductRepository.aggregate_product(
        task_number=task_number, product_code=product_code
    )
    return result
