#!/usr/bin/python3
"""Module 14: model_city_fetch_by_state
script that  prints all `City` objects from the database `hbtn_0e_14_usa`

Your script should take 3 arguments: `<mysql username>`,
                                       `<mysql password>` and
                                       `<database name>`
You must use the module SQLAlchemy
"""


from sys import argv
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Connection to Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in (session.query(City, State)
                        .filter(City.state_id == State.id)
                        .order_by(City.id).all()):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
