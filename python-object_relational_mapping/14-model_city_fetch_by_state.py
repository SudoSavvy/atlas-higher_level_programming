#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Query cities and their states
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print results
    for city in cities:
        print(f"{city.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
