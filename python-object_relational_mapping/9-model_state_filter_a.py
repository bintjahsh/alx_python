""" This module creates a script lists all State objects that
contain the letter a from the database hbtn_0e_6_usa. The script
takes 3 arguments: mysql username, mysql password and database name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.name.like('a%')).order_by(State.id)

    for id, state in query.all():
        print("{}: {}".format(id, state))
