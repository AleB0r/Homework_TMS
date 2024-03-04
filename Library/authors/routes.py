from flask import (
    redirect,
    render_template, 
    request,
    url_for,
)

from Library.app import db # Объект для работы с базой данных
from Library.authors import authors_blueprint
from Library.books.models import Author
from Library.users.utils import login_required


def main_menu():
    return render_template(
        "home/home.html"
    )


@authors_blueprint.get("/show_authors")
def show_authors():
    data = db.session.execute(db.select(Author)).fetchall()
    if data:
        return render_template(
            "show_authors.html",
            data=data
        )

@authors_blueprint.route("/add_author", methods=["GET", "POST"])
@login_required
def add_author():
    if request.method == "GET":
        return render_template(
            "add_author.html"
        )
    elif request.method == "POST":
        author_name = request.form["author_name"]
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        return redirect(
            url_for("authors.show_authors")
        )


@authors_blueprint.route("/delete_author", methods=["GET", "POST"])
@login_required
def delete_author():
    if request.method == "GET":
        authors = db.session.query(Author).all()
        return render_template("delete_author.html", authors=authors)

    elif request.method == "POST":
        author_id = request.form["author"]
        author = db.session.query(Author).get(author_id)
        if author:
            db.session.delete(author)
            db.session.commit()
        return redirect(url_for("authors.show_authors"))