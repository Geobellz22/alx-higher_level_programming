#!/usr/bin/python3
"""Script that import base_model from sqlalchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """
    state class for use in sqlalchemy inherits from Base
    declarative_Base
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullabel=False)
    state_id = Coumn(Integer, ForeignKey(State.id), nullable=False)
