""" This module creates a script that takes in the name of
a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    My_User = sys.argv[1]
    My_Pass = sys.argv[2]
    My_DB = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=My_User , passwd=My_Pass , db=My_DB)

    cursor = db.cursor()

    query = "SELECT name FROM cities WHERE state_id= (SELECT id FROM states WHERE name=%s) ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    cities_list = ""

    for city in cities:
        for i in city:
            cities_list += i

    print(cities_list)