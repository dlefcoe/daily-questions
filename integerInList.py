'''
This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
'''



import random

def generateRossMethod(n, l):
    r = random.randint(0, n -1)
    return generateRossMethod(n, l) if r in l else r

l = [0,1,2,7,8,9]
n = 8

print(generateRossMethod(n, l))



def generateFlefMethod(n, l):
    # initialise random int
    r = random.randint(0, n -1)
    while r in l:
        # make another random int
        r = random.randint(0, n -1)
    return r

l = [0,1,2,7,8,9]
n = 8

print(generateFlefMethod(n, l))





