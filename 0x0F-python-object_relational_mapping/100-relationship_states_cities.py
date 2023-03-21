#!/usr/bin/python3
"""Module 100: relationship_states_cities
script that creates `State` “California” with `City` “San Francisco” from
database `hbtn_0e_100_usa`

Your script should take 3 arguments: `<mysql username>`,
                                       `<mysql password>` and
                                       `<database name>`
You must use the module SQLAlchemy
"""


from sys import argv
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Connection to Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Read SQLAlchemy Documentation on API
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()

    session.close()
