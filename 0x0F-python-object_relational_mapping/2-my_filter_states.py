#!/usr/bin/python3
"""Module 2: my_filter_states
script that takes in an argument and displays all values in the
states table of `hbtn_0e_0_usa` where name matches the argument.
should take 4 arguments: `mysql username`,
                          `mysql password`,
                          `database name` and
                          `state name searched` (no argument validation needed)
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
    cur.execute(
        """SELECT * FROM states WHERE name LIKE
        '{:s}' ORDER BY states.id ASC""".format(argv[4]))
    query_results = cur.fetchall()
    [print(row) for row in query_results]

    cur.close()
    db.close()
