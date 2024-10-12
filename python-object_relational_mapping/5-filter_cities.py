#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa, safe from SQL injection.
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

    # Safe from SQL injection: Using parameterized query
    state_name = sys.argv[4]
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """, (state_name,))

    # Fetch all the results
    rows = cur.fetchall()

    # Print the cities in the required format
    city_names = ", ".join([row[0] for row in rows])
    print(city_names)

    # Close cursor and connection
    cur.close()
    db.close()
