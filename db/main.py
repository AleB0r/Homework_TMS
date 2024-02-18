import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import DBrepository
from menu import Menu


@click.command()
@click.option('--username', prompt='Enter your username', help='PostgreSQL username')
@click.option('--password', prompt='Enter your password', hide_input=True, help='PostgreSQL password')
@click.option('--host', default='localhost', help='PostgreSQL host')
@click.option('--port', default=5432, help='PostgreSQL port')
@click.option('--database', prompt='Enter your database name', help='PostgreSQL database name')
def main(username, password, host, port, database):
    connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    repo = DBrepository(session=session)
    menu = Menu(repo)
    while True:
        menu.show_menu()


if __name__ == "__main__":
    main()
