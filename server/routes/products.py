from fastapi import APIRouter

router_products = APIRouter(
    tags=["products"],
    prefix="/products",
)


@router_products.post(
    "/",
)
async def get_products(products):
    pass


@router_products.get("/aggregate")
async def get_aggregate(task_number, product_code):
    pass
