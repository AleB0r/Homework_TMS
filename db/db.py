from sqlalchemy.orm import Session
import sqlalchemy as sa
from repository import Repository
from models import Book, Author


class DBrepository(Repository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def show_all_books(self):
        return self.session.execute(sa.select(Book)).fetchall()

    def add_book(self, book_name: str, author_id: int):
        book = Book(name=book_name, author_id=author_id)
        self.session.add(book)
        self.session.commit()

    def update_book(self, index: int, book_name: str):
        book = self.session.query(Book).get(index)
        book.name = book_name
        self.session.commit()

    def delete_book(self, index: int):
        book = self.session.query(Book).get(index)
        if book:
            self.session.delete(book)
            self.session.commit()
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    def show_authors(self):
        return self.session.execute(sa.select(Author)).fetchall()

    def add_author(self, author_name: str):
        author = Author(name=author_name)
        self.session.add(author)
        self.session.commit()

    def find_book(self, book_name: str):
        return self.session.query(Book).filter(Book.name.ilike(f"%{book_name}%")).all()
