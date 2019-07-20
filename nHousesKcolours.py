'''

This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.

'''

import sys
import operator
import collections



nHouse = int(input('number of houses in the row >>> '))
kColour = {"red": 2, "green": 3, "blue": 2.5}
#kColour = input('number of different colours - ie. {"red":2, "green":3, "blue":2.5} >>> ')



if kColour is None:
    kColour = {"red":2, "green":3, "blue":2.5}


if len(kColour) == 1:
    print('this cannot be done')
    sys.exit()



if len(kColour) == 2:
    print('there is only one option - alternate colours')
    sortVals = list(kColour.values())
    cost = (nHouse * sortVals[0] + nHouse * sortVals[1]) / 2
    print(f'the cost is {cost}')
    sys.exit()

if len(kColour) >= 3:
    # find the lowest values in kColour
    sortVals = list(kColour.values())
    sortVals.sort()

    print('pick the lowest 2 - alternate colours')
    cost = (nHouse * sortVals[0] + nHouse * sortVals[1]) / 2
    print(f'the cost is {cost}')









