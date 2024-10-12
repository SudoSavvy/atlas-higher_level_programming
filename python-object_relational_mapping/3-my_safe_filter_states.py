#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Safe from SQL injections.
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

    # Execute SQL query using a parameterized query to prevent SQL injection
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    # Fetch all the results
    rows = cur.fetchall()

    # Print each result
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
