#!/usr/bin/python3
"""
Updates the name of a State object in the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
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

    # Query the state with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Check if the state exists
    if state_to_update:
        # Update the name of the state
        state_to_update.name = "New Mexico"
        # Commit the changes
        session.commit()

    # Close the session
    session.close()
