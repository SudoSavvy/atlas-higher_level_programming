#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa, sorted by cities.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    
    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query to fetch all cities and their states
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """)

    # Fetch all the results
    rows = cur.fetchall()

    # Print each city with its state
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
