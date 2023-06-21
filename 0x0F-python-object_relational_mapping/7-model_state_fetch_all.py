#!/usr/bin/python3
"""lists all states objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == " __main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.arg[2], sys.argv[3]),
    session = session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
