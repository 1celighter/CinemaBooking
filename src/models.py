from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

class MovieModel(Base):
    __tablename__ = "Movies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    