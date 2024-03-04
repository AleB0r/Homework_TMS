import os

from dotenv import load_dotenv
load_dotenv()


class Config:
    FLASK_DEBUG: bool = bool(os.getenv("FLASK_DEBUG")) 
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:sasha8523698@localhost:5432/postgres"
    SECRET_KEY = "8523698"
