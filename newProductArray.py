# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:09:13 2019

@author: DL


This problem was asked by Uber.

Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?


"""

import numpy as np

startArray =[1, 20, 13, 24, 15]
saP = np.prod(startArray)

prodArray = []
for e in startArray:
    prodArray.append(saP / e)
    
print(prodArray)



''' 

if the user cannot use division, then multiple all the other elements 
we can do this by removing the element from the list (array)
then perform the calculation
then add the item back into the list (array)

'''

print('same method without dividing >>')


newArray = []
for i, val in enumerate(startArray):
    print(i)
    
    poppedVal = startArray.pop(i) # remove item from list
    saP = np.prod(startArray) # calc the product
    newArray.append(saP) 
    startArray.insert(i, poppedVal) # put the item back into the list


print(newArray)


