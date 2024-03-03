from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

from server.db.models import Product


class TaskCreate(BaseModel):
    """Схема создание задания"""

    task_status: bool = Field(..., validation_alias="СтатусЗакрытия")
    shift_task_submission: str = Field(
        ..., validation_alias="ПредставлениеЗаданияНаСмену"
    )
    line: str = Field(..., validation_alias="Линия")
    shift: str = Field(..., validation_alias="Смена")
    squad: str = Field(..., validation_alias="Бригада")
    task_number: int = Field(..., validation_alias="НомерПартии")
    task_date: date = Field(..., validation_alias="ДатаПартии")
    nomenclature: str = Field(..., validation_alias="Номенклатура")
    code_ekn: str = Field(..., validation_alias="КодЕКН")
    identifier_rc: str = Field(..., validation_alias="ИдентификаторРЦ")
    start_time: datetime = Field(..., validation_alias="ДатаВремяНачалаСмены")
    end_time: datetime = Field(..., validation_alias="ДатаВремяОкончанияСмены")


class TaskRead(BaseModel):
    """Схема чтения задания"""

    id: int
    task_status: bool
    shift_task_submission: str
    line: str
    shift: str
    squad: str
    task_number: int
    task_date: date
    nomenclature: str
    code_ekn: str
    identifier_rc: str
    start_time: datetime
    end_time: datetime
    closed_at: Optional[datetime] = None
    products: List[str] = []

    @field_validator("products", mode="before")
    def convert_products(cls, value: list[Product]):
        return [product.product_code for product in value]


class TaskUpdate(BaseModel):
    """Схема обновления задания"""

    task_status: Optional[bool]
    shift_task_submission: Optional[str]
    line: Optional[str]
    shift: Optional[str]
    squad: Optional[str]
    task_number: Optional[int]
    nomenclature: Optional[str]
    code_ekn: Optional[str]
    identifier_rc: Optional[str]
