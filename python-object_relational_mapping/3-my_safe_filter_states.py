""" This module creates a script that takes in an
argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    My_User = sys.argv[1]
    My_Pass = sys.argv[2]
    My_DB = sys.argv[3]
    state_search = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=My_User , passwd=My_Pass , db=My_DB)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{:s}' COLLATE utf8mb4_0900_as_cs ORDER BY states.id ASC"
    cursor.execute(query, (state_search,))
    states = cursor.fetchall()

    for id, state in states:
        print("({:d}, '{:s}')".format(id, state))