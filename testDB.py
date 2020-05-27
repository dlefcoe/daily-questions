'''

simple json database: using the tinydb library
install: pip install tinydb


'''


import tinydb

import json
import os



db = tinydb.TinyDB('testDB.json')

# TinyDB expects the data to be Python dicts
db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})



# get all documents stored in the database
x = db.all()
print(x)


# iter over stored documents
for item in db:
    print(item)


# make a query
fruit = tinydb.Query()
x = db.search(fruit.type == 'peach')
print(x)


# make an update
db.update({'count': 10}, fruit.type == 'apple')

x = db.all()
print(x)


# remove items
db.remove(fruit.count < 5)

x = db.all()
print(x)

# purge the database (remove all data)
#db.purge()

x = db.all()
print(x)



'''

recap of usage

Inserting
db.insert(...)

Getting data
db.all()
iter(db)
db.search(query)

Updating
db.update(fields, query)

Removing
db.remove(query)
db.purge()

Querying
Query()
Query().field == 2

'''



# x = json.load('testDB.json')
#x = json.loads('testDB.json')
#print(x)

with open('testDB.json') as json_file:
    data = json.load(json_file)
    print(data)


print(data)


