from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from Library.app import db


class Book(db.Model):

    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author_id: Mapped[int] = mapped_column(db.ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(
        back_populates="books"
    )

    def __str__(self):
        return f"Book ({self.name}) by {self.author}"

    def __repr__(self):
        return str(self)
    

class Author(db.Model):

    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[List["Book"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Author: {self.name}"

    def __repr__(self):
        return str(self)