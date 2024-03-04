from flask import (
    redirect,
    render_template, 
    request,
    url_for,
)

from Library.app import db # Объект для работы с базой данных
from Library.books import books_blueprint
from Library.books.models import Book, Author
from Library.users.utils import login_required


def main_menu():
    return render_template(
        "home/home.html"
    )


@books_blueprint.route("/show_books") # Регистрируем роут в нашем модуле с указанными методами
def show_all_books():
    data = db.session.execute(db.select(Book).order_by(Book.id)).scalars().fetchall()
    return render_template(
            "show_books.html",
            data=data
        )

@books_blueprint.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    authors = db.session.query(Author).order_by(Author.id).all()
    if request.method == "GET":
        return render_template(
            "add_book.html",
            authors=authors
        )
    elif request.method == "POST":
        name = request.form["name"]
        author_id = request.form["author_id"]
        book = Book(name=name, author_id=author_id)
        db.session.add(book)
        db.session.commit()
        return redirect(
            url_for("books.show_all_books")
        )

@books_blueprint.route("/update_book", methods=["GET", "POST"])
@login_required
def update_book():
    if request.method == "GET":
        books = db.session.query(Book).all()
        return render_template("update_book.html", books=books)
    elif request.method == "POST":
        book_id = request.form["book"]
        book_name = request.form["book_name"]
        book = db.session.query(Book).get(book_id)
        if book:
            book.name = book_name
            db.session.commit()
        return redirect(url_for("books.show_all_books"))
    
@books_blueprint.route("/delete_book", methods=["GET", "POST"])
@login_required
def delete_book():
    if request.method == "GET":
        return render_template(
            "delete_book.html"
        )
    elif request.method == "POST":
        book = request.form["book"]
        book = db.session.query(Book).filter(Book.name == book).first()
        if book:
            db.session.delete(book)
            db.session.commit()
        return redirect(
            url_for("books.show_all_books")
        )
    

@books_blueprint.route("/find_book", methods=["GET", "POST"])
def find_book():

    if request.method == "GET":
        return render_template(
            "find_book.html"
        )
    
    elif request.method == "POST":
        book_name = request.form["book_name"]
        f_book = db.session.query(Book).filter(Book.name.ilike(f"%{book_name}%")).all()
        return render_template(
            "solo_book.html",
            f_book=f_book,
        )