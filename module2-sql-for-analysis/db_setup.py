#!/usr/bin python3

"""
This script will replicate today's lesson code and setup a PostgreSQL database
that we will insert the RPG data into.
"""


# Imports
import psycopg2
import sqlite3


# DATABASE SETUP
# Code to setup and connect to our database on ElephantSQL
dbname = 'kajrfesp'
user = 'kajrfesp'
password = 'H4AfXov0g_FF3G_vc1cYET3uEJ5JykMi'
host = 'isilo.db.elephantsql.com'


# Establish our connection to the database
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


# Instantiate our cursor
pg_curs = pg_conn.cursor()


"""
Create our tables to insert into our database
"""
create_char_table = """
CREATE TABLE charactercreator_character (
character_id SERIAL PRIMARY KEY,
name VARCHAR(30),
level INT,
exp INT,
hp INT,
strength INT,
intelligence INT, 
dexterity INT,
wisdom INT);
"""

"""
Other tables edited out in case they are needed later
"""
# create_armory_table = """
# CREATE TABLE armory_item (
# item_id SERIAL PRIMARY KEY,
# name VARCHAR(30),
# value INT,
# weight INT
# """
#
# create_armory_weapon_table = """
# CREATE TABLE armory_weapon(
# item_ptr_id SERIAL PRIMARY KEY,
# power INT
# """
#
# create_inv_table = """
# CREATE TABLE charactercreator_character_inventory (
# character_ptr_id SERIAL PRIMARY KEY,
# has_pet BOOL,
# energy INT
# """
#
# create_mage_table = """
# CREATE TABLE charactercreator_mage (
# character_ptr_id SERIAL PRIMARY KEY,
# has_pet BOOL,
# mana INT
# """
#
# create_thief_table = """
# CREATE TABLE charactercreator_thief (
# character_ptr_id SERIAL PRIMARY KEY,
# is_sneaking BOOL,
# energy INT
# """
#
# create_cleric_table = """
# CREATE TABLE charactercreator_cleric (
# character_ptr_id SERIAL PRIMARY KEY,
# using_shield BOOL,
# mana INT
# """
#
# create_fighter_table = """
# CREATE TABLE charactercreator_fighter (
# character_ptr_id SERIAL PRIMARY KEY,
# using_shield BOOL,
# rage INT
# """
#
# create_necro_table = """
# CREATE TABLE charactercreator_necromancer (
# mage_ptr_id SERIAL PRIMARY KEY,
# talisman_charged BOOL
# """


#Insert our table into our database
try:
    pg_curs.execute(create_char_table)
    pg_conn.commit()
except:
    print('Database table already exists!')


"""
Below we will work with sqlite3 to import our data from rpg_db.sqlite3 and insert the table 
data into our existing PostgreSQL table
"""


# Setup our conenction to our sqlite3 db
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


# FUNCTION: to send a query and return the results
def get_stuff(query):
    curs.execute(query)
    return curs.fetchall()


# FUNCTION: Defining a function to refresh connection and cursor
def refresh_connection_and_cursor(conn, curs):
    curs.close()
    conn.close()
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                             password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs


# Create our query
charQ = 'SELECT * FROM charactercreator_character LIMIT 20'

# Perform our query and get our stuff
results = get_stuff(charQ)


# Refresh the onnection and cursor before trying to load data
pg_conn, pg_curs = refresh_connection_and_cursor(pg_conn, pg_curs)


"""
The code block below is commented out to prevent rewriting to the database each time the script is ran for testing.
"""
# Insert the data into our database
# for r in results:
#     insert_character = """
#         INSERT INTO charactercreator_character
#         (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
#         VALUES """ + str(r[1:]) + ";"
#     pg_curs.execute(insert_character)
#
# pg_conn.commit()


# Printing to test that connection occured, and ensuring that the connection is cloased after running the sciprt
# Will be removed for final version
pg_conn.close()