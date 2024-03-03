import bcrypt
from flask import (
    redirect,
    render_template,
    request,
    url_for, session,
)

from Library.app import db # Объект для работы с базой данных
from Library.users import user_blueprint
from Library.users.models import User
from Library.users.utils import validate_email


@user_blueprint.route("/Registration", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_template("reg.html")
    elif request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if password and confirm password match
        if password != confirm_password:
            return render_template("reg.html", error="Passwords do not match")

        # Check if email is valid
        if not validate_email(email):
            return render_template("reg.html", error="Invalid email format")

        # Check if email already exists in the database
        if User.query.filter_by(email=email).first():
            return render_template("reg.html", error="Email already exists")

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Create a new user object
        new_user = User(email=email, password=hashed_password)

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        # Set session variable to indicate the user is logged in
        session["user_id"] = new_user.id
    return redirect(url_for("home"))  # Redirect to the home page after successful registration

@user_blueprint.route("/Authorisation", methods=["GET", "POST"])
def auth():
    if request.method == "GET":
        return render_template("auth.html")
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            session["user_id"] = user.id
            next_url = session.pop("next_url", url_for("home"))
            return redirect(next_url)
        return render_template("auth.html", error="Invalid email or password")


@user_blueprint.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("user.auth"))