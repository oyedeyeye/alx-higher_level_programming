#!/usr/bin/python3
"""Module 7: model_state_fetch_all
script that prints the first `State` objects from the database `hbtn_0e_6_usa`

Your script should take 3 arguments: `<mysql username>`,
                                       `<mysql password>` and
                                       `<database name>`
You must use the module SQLAlchemy
"""


from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == '__main__':
    # Connection to Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    # Read SQLAlchemy on more queryAPI
    first = session.query(State).order_by(State.id).first()
    print("{}: {}".format(first.id, first.name))

    session.close()
