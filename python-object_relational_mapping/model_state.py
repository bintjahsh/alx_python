"""This module is about Object-Relational Mapping.
contains the class definition of a State which is an
instance of superclass Base
"""
from sqlalchemy import Column, Integer, String

if __name__ == "__main__":
    class State(Base):
        """Creation of class State that inherits from Base and links to
        the MySQL table states.
        """
        __tablename__ = 'states'
        id = Column(Integer, unique=True, nullable=False, autoincrement=True, primary_key=True)
        name = Column(String(128), nullable=False)