#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=db_name)

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print the results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
