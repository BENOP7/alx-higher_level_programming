#!/usr/bin/python3
'''A script that fetch all cities from the database
'''

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities" +
                " INNER JOIN states ON cities.state_id=states.id " +
                "WHERE states.name='" + argv[4] + "' ORDER BY cities.id ASC")
    query_rows = cur.fetchall()

    my_str = ''
    for row in query_rows:
        my_str += (row[0])+', '
    print(my_str[:-2])

    cur.close()
    conn.close()
