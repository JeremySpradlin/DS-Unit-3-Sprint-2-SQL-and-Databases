"""
Test file for running test scripts without having to run the assignment script
"""


# IMPORTS
import sqlite3


# Setup our connection to our rpg sqlite db and return some characters
# Establish our connection and cursor
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


# FUNCTION: to send a query and return the results
def get_stuff(query):
    curs.execute(query)
    return curs.fetchall()


# Query to get our character data from our table
query = 'SELECT * FROM charactercreator_character LIMIT 20;'


# Get the results of our query from the dadtabase
results = get_stuff(query)

for r in results:
    print(r)