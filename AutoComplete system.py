
# coding: utf-8

# In[4]:


'''
This problem was asked by Twitter.
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

'''

import re

qString ='de'

stringSet = ['dog', 'deer', 'deal']
stringSetFound = []

for i in stringSet:
    z = i.find(qString)
    if z == -1:
        continue
    else:
        stringSetFound.append(i)

print(stringSetFound)
    

