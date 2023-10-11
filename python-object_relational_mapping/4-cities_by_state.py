""" This module creates a script that lists
all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    My_User = sys.argv[1]
    My_Pass = sys.argv[2]
    My_DB = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=My_User , passwd=My_Pass , db=My_DB)

    cursor = db.cursor()

    query = "SELECT cities.id, DISTINCT cities.name, states.name FROM cities INNER JOIN states ON state_id ORDER BY cities.id ASC"
    cursor.execute(query)
    states = cursor.fetchall()

    for id, state, city in states:
        print("({:d}, '{:s}', '{:s}')".format(id, state, city))