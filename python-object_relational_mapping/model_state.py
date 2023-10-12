""" This module is about Object-Relational Mapping.
contains the class definition of a State and an
instance Base = declarative_base()
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Connecting to MySQL server at 23.92.23.113 using mysql-python DBAPI 
if __name__ == "__main__":
    Base = declarative_base()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),)
    
    Base.metadata.create_all(engine)
    
    engine.connect()
    
    """A class state that inherits from Base and links to
        the MySQL table states
    """
    class State(Base):
        """A class state that inherits from Base and links to
        the MySQL table states
        """
        __tablename__ = 'states'
        id = Column(Integer, unique=True, nullable=False, autoincrement=True, primary_key=True)
        name = Column(String(128), nullable=False)