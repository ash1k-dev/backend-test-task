from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, Field

from server.schemas.products import ProductRead


class TaskCreate(BaseModel):
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
    products: List[ProductRead] = None


class TaskUpdate(BaseModel):
    task_status: Optional[bool]
    shift_task_submission: Optional[str]
    line: Optional[str]
    shift: Optional[str]
    squad: Optional[str]
    task_number: Optional[int]
    task_date: Optional[date]
    nomenclature: Optional[str]
    code_ekn: Optional[str]
    identifier_rc: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    closed_at: Optional[datetime]
