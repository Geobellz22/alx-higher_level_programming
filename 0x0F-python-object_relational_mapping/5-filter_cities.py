#!/usr/bin/python3
""" Script that takes in the name of the argument
and list all argument and lists all cities of that state,
using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM\
                        cities RIGHT JOIN states\
                        ON states.id = cities.state_id\
                        WHERE states.name = %s\
                        ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()

    print(". ".join([row[1] for row in rows]))
    cur.close()
    db.close()
