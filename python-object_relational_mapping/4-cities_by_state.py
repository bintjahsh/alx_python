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

    query = "SELECT DISTINCT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC"
    cursor.execute(query)
    states = cursor.fetchall()

    for id, city, state in states:
        print("({:d}, '{:s}', '{:s}')".format(id, city, state))