#!/usr/bin/python3
"""Module 4: cities_by_states
script that lists all `cities` from the database `hbtn_0e_4_usa`
should take 3 arguments: `<mysql username>`,
                          `<mysql password>`, and
                          `<database name>`
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
        """SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE cities.state_id=states.id
        ORDER BY cities.id ASC""")
    query_results = cur.fetchall()
    [print(row) for row in query_results]

    cur.close()
    db.close()
