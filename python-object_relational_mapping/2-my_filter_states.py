#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Arguments:
    mysql username, mysql password, database name, and state name searched.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    
    # Create a cursor object
    cur = db.cursor()

    # Use format to include user input safely into the SQL query
    # The '%s' placeholder is used to avoid SQL injection
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    # Fetch all the results
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
