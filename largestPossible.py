'''

This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.

'''

# import random as r
import itertools as itt


mylist = [1, 345, 72, 180]


def maxNumberFromList(aList):
	
	nList = itt.permutations(aList)
	
	gList = []
	for e in nList:
		
		g = ""
		
		for f in e:
			g = g + str(f)
		
		gList.append(int(g))
	
	print('the g list')	
	print(gList)
		
	mNum = max(gList)
	
	return mNum


result = maxNumberFromList(mylist)
print(result)





# ross method...
from itertools import permutations as perms

mylist = [1, 345, 72, 180]

def bigchief(alist):
    l = map(str, alist)
    return max("".join(x) for x in perms(l))

print(bigchief(mylist))




