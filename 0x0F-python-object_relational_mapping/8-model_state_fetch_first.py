#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    states = session.query(State).first()

    if states:
        print(f"{states.id}: {states.name}")
    else:
        print('Nothing')


if __name__ == '__main__':
    main()
