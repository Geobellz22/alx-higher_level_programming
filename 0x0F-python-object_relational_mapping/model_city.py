#!/usr/bin/python3
"""Script that import base_model from sqlalchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class State(Base):
    """
    state class for use in sqlalchemy inherits from Base
    declarative_Base
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullabel=False)
    state_id = column(Integer, Foreignkey("state.id"), nullable=False)
