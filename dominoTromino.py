'''
This problem was asked by Wayfair.

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.

@dlefcoe

'''



# we assume that the following is the same.
'''
aa = a    bb = b
     a    b    bb
'''


# we make a table
'''
number of dominos = d
number of trominos = t
combined dominos & trominos = (d, t)
N   d   t   (d,t)               total
0   0   0   0                   1
1   1   0   0                   1
2   2   0   0                   1
3   3   2   0                   2
4   4   0   (1,2)               2
5   5   0   (2,2)               2
6   6   4   (3,2)               3
7   7   0   (4,2) (1,4)         3
8   8   0   (5,2) (2,4)         3
9   9   6   (6,2) (3,4)         4
10  10  0   (7,2) (4,4) (1,6)   4
11  11  0   (8,2) (5,4) (2,6)   4

etc...

it is seen that for the Nth term:
    d = N
    t = 2/3 * N if N = 3m (where m = integer)

basically there is a repeating pattern.
'''

import time

t0 = time.time()
n = 1_000_000
a = []

total = 1
counter = 0
for i in range(n):
    a.append(total)
    counter += 1

    if counter == 3:
        counter = 0
        total = total + 1

print('the answer is:')
print(a)

t1 = time.time()
print('the time taken:', round(t1-t0,3), 'seconds')

print(len(a))
print(a[999_999])


