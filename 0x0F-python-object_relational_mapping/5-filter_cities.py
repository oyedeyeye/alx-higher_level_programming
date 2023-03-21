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
        """SELECT cities.id, cities.state_id, cities.name, states.name 
        FROM cities, states
        WHERE cities.state_id =
        (SELECT states.id
        FROM states
        WHERE states.name LIKE %s)
        ORDER BY cities.id ASC""", (argv[4], ))
    query_results = cur.fetchall()
    # print([row for row in query_results])
    print(", ".join([row[2] for row in query_results if row[3] == argv[4]]))

    cur.close()
    db.close()
