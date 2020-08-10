#!/usr/bin/python
"""
This python script will perform queries against the rpg_db.sqlite3 database in order to answer the following
questions:

1) How many total Characters are there?
2) How many of each specific subclass?
3) How many total items?
4) How many of the items are weapons?  How many are not?
5) How many items does each character have? (Return first 20 rows)
6) How many Weapons does each character have? (Return first 20 rows)
7) On average, how many items does each Character have?
8) On average, how many Weapons does each character have?
"""


#Imports
import sqlite3


#Establish our connection and cursor
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


#FUNCTION: to send a query and return the results
def get_stuff(query):
    curs.execute(query)
    return curs.fetchall()


#Question #1
#Create our Query
query1 = 'SELECT COUNT(*) FROM charactercreator_character;'

#Get the results from our first query and store it in a variable
results = get_stuff(query1)
print('QUESTION 1')
print('Total number of characters: {}'.format(results[0][0]))
#print a blank line between questions
print('')


#Question #2
#Create our query
clericQ = 'SELECT COUNT(*) FROM charactercreator_cleric;'
fighterQ = 'SELECT COUNT(*) FROM charactercreator_fighter;'
mageQ = 'SELECT COUNT(*) FROM charactercreator_mage;'
necroQ = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
thiefQ = 'SELECT COUNT(*) FROM charactercreator_thief;'

#Get our results
clerics = get_stuff(clericQ)
fighters = get_stuff(fighterQ)
mages = get_stuff(mageQ)
necros = get_stuff(necroQ)
thiefs = get_stuff(thiefQ)

#Print statements
print('QUESTION 2')
print('Total number of each subclass:')
print('Clerics: {}'.format(clerics[0][0]))
print('Fighters: {}'.format(fighters[0][0]))
print('Mages: {}'.format(mages[0][0]))
print('Necromancers: {}'.format(necros[0][0]))
print('Thiefs: {}'.format(thiefs[0][0]))
#Print a blank line between questions
print('')


#Question #3
#Create our query
query3 = 'SELECT COUNT(*) FROM armory_item;'

#Get our results
items = get_stuff(query3)

#Print Statements
print('QUESTION 3')
print('Total number of items: {}'.format(items))
print('')


#Question #4
#Create our query
weaponsQ = 'SELECT COUNT(*) FROM armory_weapon;'

#Get our results
weapons = get_stuff(weaponsQ)
not_weapons = items[0][0] - weapons[0][0]

#Print Statements
print('QUESTION 4')
print('Total number of weapons: {}'.format(weapons[0][0]))
print('Total number of items that are not weapons: {}'.format(not_weapons))
print('')


#Question #5
#Create our query
char_itemsQ = """
SELECT name, COUNT(*) as item_id_count
FROM charactercreator_character AS cc, charactercreator_character_inventory AS ci
WHERE cc.character_id = ci.character_id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 20;
"""

#Get our restuls
results = get_stuff(char_itemsQ)

#Print Statements
print('QUESTION 5')
print('Players with the most items:')
for r in results:
    print('{} has {} items.'.format(r[0], r[1]))
print('')


#Question #6
#Create our query
query = """
SELECT name, COUNT(item_ptr_id) as weapon_count
FROM (SELECT name, item_id
FROM charactercreator_character AS cc,
charactercreator_character_inventory AS ci
WHERE cc.character_id = ci.character_id),
armory_weapon AS aw
WHERE item_id = item_ptr_id
GROUP BY name
ORDER BY 2 DESC
LIMIT 20;
"""

#Get our results
results = get_stuff(query)

#Print our results
print('QUESTION 6')
print('Our top weapon holders:')
for r in results:
    print('{} has {} weapons.'.format(r[0], r[1]))
print('')


#Question #7
#Create our query
query = """
SELECT AVG(item_id_count)
FROM (SELECT name, COUNT(*) as item_id_count
FROM charactercreator_character AS cc, charactercreator_character_inventory AS ci
WHERE cc.character_id = ci.character_id
GROUP BY 1);
"""

#Get our results
results = get_stuff(query)

#Print our results
print('QUESTION 7')
print('{} is the average number of items each character has.'.format(results[0][0]))
print('')


#Question #8
#Create our query
query = """
SELECT AVG(weapon_count)
FROM (SELECT name, COUNT(item_ptr_id) as weapon_count
FROM (SELECT name, item_id
FROM charactercreator_character AS cc,
charactercreator_character_inventory AS ci
WHERE cc.character_id = ci.character_id),
armory_weapon AS aw
WHERE item_id = item_ptr_id
GROUP BY name)
"""

#Get our results
results = get_stuff(query)

#Print our results
print('QUESTION 8')
print('{} is the average number of items each character has.'.format(results[0][0]))


