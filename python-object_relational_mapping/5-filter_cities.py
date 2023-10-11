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

    query = "SELECT * FROM cities.name JOIN states ON cities.state_id=states.id WHERE states.name={} ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    cities_list = ""

    for city in cities:
        if city != cities[-1]:
            cities_list += "{:s},".format(city)
        else:
            cities_list += "{:s}".format(city)