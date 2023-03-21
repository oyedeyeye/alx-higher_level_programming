#!/usr/bin/python3
"""Module: relationship_city
Script that contains the class definition of a `City`
and an instance Base = declarative_base():

City class:
    inherits from Base
    links to the MySQL table `cities` Using `SQLAlchemy`
    class attribute `id` that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    class attribute `name` that represents a column of a string with
    maximum 128 characters and cant be null
    class attribute state_id that represents a column of an integer,
    cant be null and is a foreign key to states.id
"""


import model_state
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Declarative base class
Base = declarative_base()


# City inheiting from model_state Base class
class City(Base):
    """Inherits from the model_state' Base class and
    Links to the MySQL table `cities`

    Attributes:
        __tablename__ (str): name of MySQL table to store cities
        id (sqlalchemy.Integer): The city's id, a primary key
        name (sqlalchemy.String): the name of the city
        state_id = A foreign key relating to model_state.State.id
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"),
                      nullable=False)
