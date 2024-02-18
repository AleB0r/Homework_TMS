from typing import List
import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    def __init__(self, id=None, name=None, author_id=None):
        self.id = id
        self.name = name
        self.author_id = author_id

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(
        back_populates="books"
    )

    def __str__(self):
        return f"Book ({self.name}) by {self.author}"

    def __repr__(self):
        return str(self)


class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[List["Book"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Author: ({self.name})"

    def __repr__(self):
        return str(self)
