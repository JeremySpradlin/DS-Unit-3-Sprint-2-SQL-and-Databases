#!/usr/bin python3
"""
This script will read in our rpg database and store the info as documents into our MongoDB cloud.
"""

# IMPORTS
import sqlite3
import pymongo


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


# FOR LOOP: Iterates through the results, transforming them into JSON objects
# To be inserted into MangoDB
all_docs = []
for r in results:
    doc = {
        'character_id': r[0],
        'name': r[1],
        'level': r[2],
        'exp': r[3],
        'hp': r[4],
        'strength': r[5],
        'intelligence': r[6],
        'dexterity': r[7],
        'wisdom': r[8]
    }
    all_docs.append(doc)


# Create our connection to our MangoDB
client = pymongo.MongoClient("mongodb+srv://erbun:npbaccmD46SvNDl9@cluster0.2zf9d.mongodb.net/"
                             "test?retryWrites=true&w=majority")
db = client.test


# Insert our rpg character dictionary into the mongo db
# db.test.insert_many(all_docs)  # Comment out for testing


# Run a test query to verify that it sees one of our characters
print(*db.test.find(), sep='\n')
