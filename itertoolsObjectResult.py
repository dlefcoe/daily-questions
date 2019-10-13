'''

itertools.product() is a single use object.

Internally, they are like a pointer that points to an item in a linked list 
that moves up once every time a new item is fetched (through the next function).

'''


import itertools as it


def loopsThings(*lsts):


    # list of possibilities
    allPossible = [x for x in it.product(a, b, c)]
    

    for i in allPossible:
        print('first pass', i)


    for i in allPossible:
        print('second pass', i)
       
    return


a = [3, 5, 10]
b = [1, 9, 15]
c = [4, 8]

loopsThings(a, b, c)

