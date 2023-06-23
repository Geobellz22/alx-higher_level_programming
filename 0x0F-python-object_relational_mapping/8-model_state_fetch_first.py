#!/usr/bin/python3
""" print the first state"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if  __name__ == "__main__":
     engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                             .format(sys.argv[1], sys.argv[2], sys.argv[3]))
     Session = sessionmaker(bind=engine)
     session = Session()
     state = session.query(State).order_by(State.id).first()
     if state is None:
         print("{}: {}".format(state.id), (state.name))
