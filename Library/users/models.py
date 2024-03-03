from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.schema import UniqueConstraint
from Library.app import db


class User(db.Model):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]

    __table_args__ = (UniqueConstraint('email', name='unique_email'),)

    def __str__(self):
        return f"User ({self.email})"

    def __repr__(self):
        return str(self)