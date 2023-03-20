#!/usr/bin/python3
"""Module 1: filter_states
script that lists all states with a name
starting with N (upper N) from the database `hbtn_0e_0_usa`
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    # Database connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    # SQL statement execution
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    query_results = cur.fetchall()
    for i in query_results:
        print(i)

    cur.close()
    db.close()
