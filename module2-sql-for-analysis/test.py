#!/usr/bin python3

"""
This script is for ease of testing
"""


#Imports
import psycopg2


#DATABASE SETUP
#Code to setup and connect to our database on ElephantSQL
dbname = 'kajrfesp'
user = 'kajrfesp'
password = 'H4AfXov0g_FF3G_vc1cYET3uEJ5JykMi'
host = 'isilo.db.elephantsql.com'


#Establish our connection to the database
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


#Instantiate our cursor
pg_curs = pg_conn.cursor()

query = """
SELECT *
FROM charactercreator_character
"""

pg_curs.execute(query)
results = pg_curs.fetchall()

print(results)


pg_curs.close()
pg_conn.close()