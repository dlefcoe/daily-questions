
# %%

'''

The Collatz Conjecture is the simplest math problem no one can solve 
— it is easy enough for almost anyone to understand but notoriously 
difficult to solve.

given any number:
    if odd: n = n*3 + 1
    if even: n = n/2

the final value is always a [4,2,1] loop.

'''

import matplotlib.pyplot as plt
from numpy import average, std
import time

def f(n):
    ''' the function itself: 
    
    given an input n, what is the next value
    '''
    if n % 2 == 0:
        # have an even number
        v = int(n/2)
        return v
    if n%2 !=0:
        # have an odd number
        v = n * 3 + 1
        return v


def number_iterations(n):
    ''' given a number n, how many steps until a solution is reached

    args:
        n (int): input number

    return:
        counter: the number of loops until 1 is reached 
    
    '''
    counter = 0
    while n > 1:
        counter += 1
        n = f(n)
    
    return counter



def num_iterations_mem(n: int, d:dict):
    '''
    given a number n, how many steps until a solution is reached
    but this time using dictionary for memory. This method is faster 
    because previous values are now stored in memory (dict).

    args:
        n (int): input number that we are testing
        d (dict): memory of previous values

    return:
        counter (int): the number of loops until 1 is reached 
    
    '''
    counter = 0
    while n > 1:
        counter += 1
        if n in d.keys():
            # we know the path to get to 1 from here
            counter = counter + d[n]
            return counter

        n = f(n)

    return counter


def old_method():
    ''' this was the old method, 4 seconds slower for 10_000 loop '''
    m = [n]  # 4,2,1 loop

    for i in range(2):
        # first 3 elements of the loop
        n = f(n)
        m.append(n)
        # print(m)

    for i in range(2, 1000):
        # all the other loops
        n = f(n)
        # print(n)
        m.pop(0)
        m.append(n)
        # print(m)
        if m == [4,2,1]:
            return i


print('counter starting....')
t0 = time.time()
d = {}
for n in range(1_000_000):
    # n = 22  # initial number
    # x = number_iterations(n)
    x = num_iterations_mem(n, d)
    # print(n, x)
    d[n] = x
t1 = time.time()

print(f'the process took {round(t1-t0, 3)} seconds')

# print(d.values())

# how many None's
print('number of nones', len([x for x in d.values() if x==None]) )
number_answers = [x for x in d.values() if x!=None]
print('max', max(number_answers))
print('avg', round(average(number_answers)))
print('std', round(std(number_answers)))

# line chart
plt.plot(d.keys(), d.values())
plt.xlabel('number n')
plt.ylabel('number of iterations')
plt.title('Collatz Conjecture - iterations for n')
plt.show()

# histogram 
v = [x if x is not None else 0 for x in d.values()]
plt.hist(v, bins=50, rwidth=0.75)
plt.xlabel('number number of iterations')
plt.ylabel('frequency')
plt.title('Collatz Conjecture - iterations for n')
plt.show()

