'''

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

'''

import sys
import math as m


nStair = int(input('max number of stairs: (default = 4)') or '4') # the number of stairs to climb
stMax = int(input('max number of steps: (default = 2)') or '2')  # max number of steps at a time
stAllow = list(range(1,stMax+1))    # list of allowable values,  ie. st = 4 => 1, 2, 3, 4

print(stAllow)
print(nStair)


# before we begin, lets make sure there are enough stairs
if nStair >= stMax:
    pass
else:
    print('number stairs needs to be larger than max step size....')
    print('either [1] increase stairs or [2] reduce max step size')
    print('thank you !')
    sys.exit()



print('the factorial >>', m.factorial(nStair))
nPr = m.factorial(nStair) / m.factorial(stMax)
nCr = m.factorial(nStair) / m.factorial(stMax) / m.factorial(nStair - stMax)
print('the nPr >>', int(nPr))




'''
some thoughts on the matter:

the combinations 2, 2 are
11
2
=> 2


the combinations 3, 2 are
111
21
12
=> 3


the combinations 4, 2 are
1111
211
121
112
22
=> 5

the combinations 5, 2 are
11111
2111
1211
1121
1112
221
212
122
=> 8

the combinations 6, 2 are
111111
21111
12111
11211
11121
11112
2211
2121
2112
1221
1212
1122
222
=> 13

We see a pattern emerging.

V(n) = V(n-1) + v(n-1)


This means that we just need to know the values of the first 2 steps.
The interative.

'''

# find different combinations
combi = 0

# lets take the base case
if stMax == 1:
    combi = 1   # there is only one way

if stMax == 2:
    # the is contingent on the number of stairs via the recursive formula
    # V(n) = V(n-1) + v(n-1)
    if nStair == 2:
        combi = 2
    elif nStair ==3:
        combi = 3
    else:
        # enter the recursion nTimes
        nTimes = nStair - 3
        prevTerm = 3
        prev2Term = 2
        for i in range(nTimes):
            nThTerm = prevTerm + prev2Term
            prev2Term = prevTerm
            prevTerm = nThTerm
            combi = nThTerm

    

print('number of combinations: ' + str(combi))


