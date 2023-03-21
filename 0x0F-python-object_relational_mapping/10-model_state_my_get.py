#!/usr/bin/python3
"""Module 10: model_state_my_get
Prints `State` object with `name` passed as
argument from database `hbtn_0e_6_usa`

Your script should take 4 arguments: `<mysql username>`,
                                       `<mysql password>`
                                       `<database name>` and
                                       `<state name to search>`
                                       (SQL injection free)
You must use the module SQLAlchemy
"""


from sys import argv
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Connection to Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Read SQLAlchemy on more queryAPI
    found = False
    for state in session.query(State).order_by(State.id).all():
        if state.name == argv[4]:
            print("{}".format(state.id))
            found = True
            break

    if found is False:
        print("Not found")

    session.close()
