from flask import Flask

from Library.app.config import Config


app = Flask(__name__)

app.config.from_object(Config) # Конфигурация приложения и его компонентов

from Library.app.db import db

db.init_app(app) # Подключение базы данных к приложению


from Library.books import books_blueprint
from Library.authors import authors_blueprint
from Library.users import user_blueprint

app.register_blueprint(
    books_blueprint,
    url_prefix="/books",
) 

app.register_blueprint(
    authors_blueprint,
    url_prefix="/authors",
) 

app.register_blueprint(
    user_blueprint,
    url_prefix="/user",
)
from Library.app.routes import *
