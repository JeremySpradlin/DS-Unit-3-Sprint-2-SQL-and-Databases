#!/usr/bin/python3

"""
This script will read in from the buddymove_holidyiq.csv to create a dataframe,
and then using the sqlite3 module, open a connection to a new database and
insert the data into the database
"""

#IMPORTS
import pandas as pd
import sqlite3


#Read our csv file into our dadta frame
df = pd.read_csv('buddymove_holidayiq.csv')


#Establish our connection and cursor
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()


#FUNCTION: to send a query and return the results
def get_stuff(query):
    curs.execute(query)
    return curs.fetchall()

#Send the dataframe to the database
df.to_sql('buddymove_holidayiq', con=conn)


#QUESTION 1
#Count how many rows you have
#Create query
query = """
SELECT COUNT(*) 
FROM buddymove_holidayiq
"""

#Get our results
result = get_stuff(query)

#Print out our results
print('')  #To clear a space between any output messages from tha pandas operation above
print('There are {} rows in the database.'.format(result[0][0]))
print('')  #Clearing a space before the next answer as per usual.


#QUESTION 2
#How many users reviewed at least 100 in both Nature and Shopping
#Create query
query = """
SELECT COUNT(*) 
FROM buddymove_holidayiq
WHERE Nature >= 100 AND Shopping >= 100;
"""

#Get our results
result = get_stuff(query)

#Print our results
print('THere are {} people who reviewed at least 100 in the categories of Nature and Shopping.'.format(result[0][0]))
