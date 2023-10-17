'''
estimate the value of e in pyhton

- Select numbers between 0 and 1 randomly until sum is > 1. 
- The expected # of selections needed is equal to e.
- The `measured average`.

'''

import random
import math


def value_of_e():
    ''' get the value of e '''
    
    n = 1_000
        
    sum_count = 0
    for i in range(n):
        s, counter = 0, 0
        while s <=1:
            s += random.random()
            counter += 1
        sum_count += counter

    e = sum_count / n

    return e

e = value_of_e()

print(f'{e=}, difference = {math.e - e:2f}')
