'''

This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. 
That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |
| 2 | 4 | 6 | 8 | 10 | 12 |
| 3 | 6 | 9 | 12 | 15 | 18 |
| 4 | 8 | 12 | 16 | 20 | 24 |
| 5 | 10 | 15 | 20 | 25 | 30 |
| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.


'''



from functools import reduce

def factors(n):
    ''' returns a dict of factors for n '''    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def factorsInRows(rows, numToFind):


    v = sorted(factors(numToFind))
    print('sorted list:',v)
    
    counter = 0
    for i in v:
        if i <= rows:
            counter += 1
        else:
            return counter

    return counter



print('the answer is:', factorsInRows(10, 100))

print('the answer is:', factorsInRows(100, 10))


