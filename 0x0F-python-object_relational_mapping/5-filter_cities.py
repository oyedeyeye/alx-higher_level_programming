#!/usr/bin/python3
"""Module 5: filter_cities
script that takes in the name of a state as an argument and
lists all `cities` of that state, using the database `hbtn_0e_4_usa`
should take 4 arguments: `<mysql username>`,
                          `<mysql password>`, and
                          `<database name>`
                          `<state name>` (SQL injection free!)
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
        """SELECT cities.name 
        FROM cities
        WHERE cities.state_id=
        (SELECT id
        FROM states
        WHERE name= %s)
        ORDER BY cities.id ASC""", (argv[4], ))
    query_results = cur.fetchall()
    for row in query_results:
        if row is not query_results[-1]:
            print("{:s}".format(row[0]), end=", ")
        else:
            print("{:s}".format(row[0]))

    cur.close()
    db.close()
