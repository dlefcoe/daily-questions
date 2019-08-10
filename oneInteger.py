

'''

This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, 
find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
Please see the badasses example at the bottom for what O(N) time and O(1) space mean.

'''

import time as t
import sys

start = t.time()

arr = [6, 1, 3, 3, 3, 6, 6]
arr = [13, 19, 13, 13]
arr = [13, 19, 13, 13, 20, 20, 20, 15, 15, 15]

arr.sort()


# sorted 1,3,3,3,6,6,6
print('sorted array:', arr)


def findTheVal(arr):
    # make sure array lenght is sufficient
    if len(arr) < 4:
        return 'length of array is too small'

    # check the start
    if arr[0] == arr[1]:
        # the first element is good
        pass #print(arr[0], 'is fine')
    else:
        # print('the single value is:', arr[0])
        return arr[0]



        # check the end
    if arr[len(arr)-1] == arr[len(arr)-2]:
        # the last element is good
        pass #print(arr[len(arr)-1], 'is fine')
    else:
        # print('the single value is:', arr[len(arr)-1])
        return arr[len(arr)-1]
        

    # work the middle
    for i in range(2,len(arr)-2):
        if arr[i-1] == arr[i] or arr[i] == arr[i+1]:
            pass #print(arr[i], 'is fine')
        else:
            # print('the single value is',arr[i])
            return arr[i]
    
print('the single value is >>>',findTheVal(arr))

end = t.time()

print('--- end ---')
print('time taken: ', end - start)









'''
below is an example of O(1) vs O(n)
the key difference is that O(1) is a hash table which directly extracts a piece of memory as opposed to looping through a list
'''

def bdass():



    # O(1) vs O(n) constant time vs linear time

    badasses = [
    'jon snow',
    'arya stark',
    'sansa stark',
    'brianne of tarth',
    'denyraius gargarian'
    ]



    characterToSearchFor = 'jon snow' #'jon snow'

    # O(n) - linear time
    # n refers to the number of items in the list
    for badass in badasses:
        print(badass)
        if characterToSearchFor == badass:
            break


    # hashmap (dictionary)
    # O(1)
    badassesDict = {
            'jon snow':1,
            'arya stark':2,
            'sansa stark':3,
            'brianne of tarth:1':4,
            'denyraius gargarian':5
    }

    try:
        doesExist = badassesDict[characterToSearchFor]
        print(doesExist)
    except:
        print(characterToSearchFor, 'does not exist')


    # my question is this.
    # the programmer still has to, in some way create the discionary. This takes time.



        
