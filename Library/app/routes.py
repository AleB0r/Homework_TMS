from flask import render_template

from Library.app import app


@app.route("/")
def home():
    return render_template(
        "home/home.html"
    )
