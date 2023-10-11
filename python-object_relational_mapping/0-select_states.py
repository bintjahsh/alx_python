""" This module creates a script that lists all states
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    My_User = sys.argv[1]
    My_Pass = sys.argv[2]
    My_DB = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=My_User , passwd=My_Pass , db=My_DB)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id")
    states = cursor.fetchall()

    for id, state in states:
        print("({:d}, {:s})".format(id, state))