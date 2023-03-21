#!/usr/bin/python3
"""Module 102: relationship_cities_states_list
script that lists all `City` objects, and corresponding `City` objects,
contained in database `hbtn_0e_101_usa`

Your script should take 3 arguments: `<mysql username>`,
                                       `<mysql password>` and
                                       `<database name>`
You must use the module SQLAlchemy
Use `state` relationship to access to `State` object linked to `City` object
Results must be sorted in ascending order by `cities.id`
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
    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
