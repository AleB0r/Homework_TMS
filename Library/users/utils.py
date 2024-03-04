from flask import session, redirect, url_for, request
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            session["next_url"] = request.url
            return redirect(url_for("user.auth"))
        return f(*args, **kwargs)
    return decorated_function


def validate_email(email):
    import re
    email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(email_regex.match(email))