from flask import Blueprint


user_blueprint = Blueprint(
    "user",
    __name__,
    template_folder="templates",
)


from Library.users.routes import *