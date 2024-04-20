#!/usr/bin/python3
'''A script that lists all states from the database having name starting with
   with N
'''

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name like binary 'N%';")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
