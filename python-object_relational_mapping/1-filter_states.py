""" This module creates a script that lists all states
with a name starting with N (upper N) from the database
hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    My_User = sys.argv[1]
    My_Pass = sys.argv[2]
    My_DB = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=My_User , passwd=My_Pass , db=My_DB)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8mb4_0900_as_cs ORDER BY states.id ASC")

    states_N = cursor.fetchall()
    for id, state in states_N:
        print("({:d}, '{:s}')".format(id, state))
