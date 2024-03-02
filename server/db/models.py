from datetime import date, datetime

from sqlalchemy import DateTime, ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    """Базовая модель"""

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


class Task(Base):
    """Модель сменного задания"""

    task_status: Mapped[bool]
    shift_task_submission: Mapped[str]
    line: Mapped[str]
    shift: Mapped[str]
    squad: Mapped[str]
    task_number: Mapped[int]
    task_date: Mapped[date]
    nomenclature: Mapped[str]
    code_ekn: Mapped[str]
    identifier_rc: Mapped[str]
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    closed_at: Mapped[datetime | None]
    products: Mapped[list["Product"]] = relationship(back_populates="task")

    __table_args__ = (UniqueConstraint("task_number", "task_date"),)


class Product(Base):
    """Модель продукта"""

    product_code: Mapped[str] = mapped_column(unique=True)
    task_number: Mapped[int]
    task_date: Mapped[date]
    is_aggregated: Mapped[bool] = mapped_column(default=False)
    aggregated_at: Mapped[datetime | None]
    task: Mapped["Task"] = relationship(back_populates="products")

    __table_args__ = (
        ForeignKeyConstraint(
            ["task_number", "task_date"], [Task.task_number, Task.task_date]
        ),
    )
