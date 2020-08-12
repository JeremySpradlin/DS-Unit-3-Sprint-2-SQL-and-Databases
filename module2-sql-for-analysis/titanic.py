#!/usr/bin python3

"""
This script is for loading the titanic data from csv, connecting to our Elephant database, creating a table,
and then transfering teh data to the table.
"""

import psycopg2
import pandas as pd


"""
First we need to read in and verify the transform of our data for inserting
into our database.
"""


# Import the csv file into a dataframe and print it's head to test
df = pd.read_csv('titanic.csv')
print(df.head())
print(df.dtypes)
print(df)

