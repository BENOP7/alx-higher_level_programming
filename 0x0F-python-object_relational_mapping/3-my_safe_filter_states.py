#!/usr/bin/python3

import MySQLdb
from sys import argv


def main():
    MY_HOST = 'localhost'
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    MY_PORT = 3306
    state_name = argv[4]

    db = MySQLdb.connect(
        host=MY_HOST, user=MY_USER,
        passwd=MY_PASS, db=MY_DB, port=MY_PORT)

    cur = db.cursor()
    my_q = f"select * from states \
        where states.name='{state_name}' order by states.id"
    cur.execute(my_q)

    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
