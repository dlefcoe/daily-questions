'''

things about the prem league
this project uses pandas to pull web data in place of requests

'''

import requests # dont use
import json # dont use
import pandas as pd

url = 'https://www.bbc.co.uk/sport/football/tables'
# req = requests.get(url) # dont use
# data = req.text
# jsn = req.json

# j = json.dumps(data)


#print(j)


premTable = pd.read_html(url)
premTable = premTable[0]

#print(premTable.head(6))

# print(premTable)

# inspect datatypes of the columns
# print(premTable.dtypes) # all are pandas objects, which are strings.


# shape of the table
print(premTable.shape) # we see the table is 21 rows, but should be 20


# drop the last row
premTable.drop(premTable.tail(1).index, inplace=True)

# convert to correct types
premTable[['P','W','D','L','F','A','GD','Pts']] = premTable[['P','W','D','L','F','A','GD','Pts']].apply(pd.to_numeric, errors='coerce', downcast='integer')
# print(premTable.dtypes)

# change column headings to something logical for humans
premTable.rename(columns={'Unnamed: 0':'Position'}, inplace=True)
premTable.rename(columns={'Unnamed: 1':'Position move'}, inplace=True)

# print(premTable.tail(3))

# create new columns
premTable['GR'] = round(premTable['F']/premTable['A'],1)
premTable['GPG'] = round(premTable.F/premTable.P,1)
premTable['GcPG'] = round(premTable.A/premTable.P,1)

# reorder the data
premTable = premTable[['Position', 'Team', 'P', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts', 'GR', 'GPG','GcPG']]


#print(premTable.head(5))
print(premTable)



