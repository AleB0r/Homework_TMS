from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import DBrepository
from menu import Menu

if __name__ == "__main__":
    engine = create_engine('postgresql://postgres:sasha8523698@localhost:5432/postgres')
    Session = sessionmaker(bind=engine)
    session = Session()
    repo = DBrepository(session=session)
    menu = Menu(repo)
    while True:
        menu.show_menu()
