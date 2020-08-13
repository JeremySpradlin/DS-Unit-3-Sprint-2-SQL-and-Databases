"""
Module4 Assignment
Answer questions by querying our datasets
"""


# IMPORTS
import psycopg2
import pymongo

"""
This script will query our titanic databse using postgres to answer the following questions:

1) How many passengers survived, and how many died?
2) How many passengers were in each class?
3) How many passengers survived/died within each class?
4) What was the average age of survivors vs nonsurvivors?
5) What was the average age of each passenger class?
6) What was the average fare by passenger class? By survival?
7) How many siblings/spouses aboard on average, by passenger class? By survival?
8) How many parents/children aboard on average, by passenger class? By survival?
9) Do any passengers have the same name?

(Bonus! Hard, may require pulling and processing with Python) How many married 
couples were aboard the Titanic? Assume that two people (one Mr. and one Mrs.) with the same 
last name and with at least 1 sibling/spouse aboard are a married couple.
"""


# Setup connection to our elephantSQL DB
# Credentials
dbname = 'cskdkelm'
user = 'cskdkelm'
password = 'FxkrjJmEHV3Y50dmj-kRVO8BNok9S3Ad'
host = 'drona.db.elephantsql.com'

# Connect to the cloud and create our cursor
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()


# FUNCTION: to send a query and return the results
def get_stuff(query):
    curs.execute(query)
    return curs.fetchall()


# QUESTION 1
q = """
SELECT COUNT(*) FROM Titanic
WHERE survived = 0
"""
results = get_stuff(q)
print(results[0][0])




# Test query
q = """
SELECT COUNT(*) FROM Titanic LIMIT 1
"""

results = get_stuff(q)
print(results)

conn.close()