from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Todo(Base):

    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(200)
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    priority: Mapped[int] = mapped_column(
        Integer
    )