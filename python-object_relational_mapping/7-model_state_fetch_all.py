""" This module creates a script that lists all State
objects from the database hbtn_0e_6_usa. The script takes
3 arguments: mysql username, mysql password and database name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
Session = sessionmaker(bind=engine)

query = Session.query(State.id, State.name).order_by(State.id)
print(query)
# print("{:d}: {:s}".format(State.id, State.name))
