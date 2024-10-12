#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base
Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table 'states'
    """
    __tablename__ = 'states'

    # Define attributes
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
