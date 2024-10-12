#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine to connect to MySQL
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query for states containing the letter 'a' and sort by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
