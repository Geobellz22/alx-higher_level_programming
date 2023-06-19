#!/usr/bin/python3
"""Script that contains state class and Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):

    """Class with id and name attributes of each state"""
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True,\n primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
