'''

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, 
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, 
since we can't split it up into two subsets that add up to the same sum.

'''


import itertools as it
import time as t
import random as r

m = [15, 5, 20, 10, 35, 15, 10]
m = [1,1,1,1,1,1,1,1,1, 10] # top heavy list
m = [1,1,1,1,1,1,1,1,1, 10, 15] # double top heavy list
m = [r.randint(0,100) for x in range(20)]




def startCode(m):
    print('here is the start list:')
    print(m)
    return 1


def partMulti(m):
    """ code to run multiset """
    m.sort()
    
    # check is sum is odd:
    if sum(m) %2 == 0: # even number
        semiSum = sum(m) / 2
    else: # odd number
        print('ODD list: cannot split into 2 equal subsets.')
        return 1


    print('the semi-sum is:',semiSum)
    

    # throw out a big top number
    if m[-1] > semiSum:
        print('the list element', m[-1], 'is top heavy - cannot solve')
        return 0
    elif m[-1] == semiSum:
        print('FOUND: element', m[-1], 'which is largest number')
        return 1

    # if there are 2 big numbers
    if m[-1] + m[-2] > semiSum:
        # split the 2 large numbers and seek a solution
        print('double top found')
        # ==== need to add code here ==========
        pass
    

    # iterate the numbers to find semiSum
    print('iterating combinations to find the semi-sum...')
    sucess = False

    for j in range(2, len(m)):
        # iterate through increasing combinations

        for i in it.combinations(m,j):
            # print('element:', i, '  --- sum:', sum(i) )
            if sum(i) == semiSum:
                print('FOUND: element:', i, '  --- sum:', sum(i))
                sucess = True
                return 1

    if sucess == False:
        print('the list cannot split into 2 equal subsets.')

    return 1


# run the functions

start = t.time()

startCode(m)
partMulti(m)

end = t.time()

print('time take:', round(end - start, 3), 'seconds')

