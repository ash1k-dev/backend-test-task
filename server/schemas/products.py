from datetime import date

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    """Схема создания продукта"""

    product_code: str = Field(..., validation_alias="УникальныйКодПродукта")
    task_number: int = Field(..., validation_alias="НомерПартии")
    task_date: date = Field(..., validation_alias="ДатаПартии")


class ProductRead(BaseModel):
    """Схема чтения продукта"""

    product_code: str = Field(..., validation_alias="УникальныйКодПродукта")
