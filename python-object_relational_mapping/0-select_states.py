#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The MySQL username.
    mysql_password: The MySQL password.
    database_name: The database name.

The script connects to a MySQL database running on localhost at port 3306,
executes a query to fetch all states, and prints them in ascending order
by the state's id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the query to select all states, ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the executed query
    states = cursor.fetchall()

    # Print each state in the format (id, name)
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
