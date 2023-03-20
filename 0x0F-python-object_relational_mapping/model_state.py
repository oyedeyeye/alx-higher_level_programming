#!/usr/bin/python3
"""Module 6: model_state
Script that contains the class definition of a State
and an instance Base = declarative_base():

State class:
    inherits from Base Tips
    links to the MySQL table states Using `SQLAlchemy`
    class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a string with
    maximum 128 characters and can’t be null
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Declarative base class
Base = declarative_base()


# State mapping using the base
class State(Base):
    """Inherits from the Base class and
    Links to the MySQL table states

    Attributes:
        __tablename__ (str): name of MySQL table to store States
        id (sqlalchemy.Integer): The state's id, a primary key
        name (sqlalchemy.String): the name of the state
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
