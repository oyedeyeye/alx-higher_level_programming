#!/usr/bin/python3
"""Module 13: model_state_delete_a
Deletes all `State` objects with name
containing letter `a` from database `hbtn_0e_6_usa`

Your script should take 3 arguments: `<mysql username>`,
                                       `<mysql password>` and
                                       `<database name>`
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

    # Update a DB record
    session.query(State).filter(State.id == 2).update(
                {"name": "New Mexico"}, synchronize_session="fetch")
    session.commit()

    session.close()
