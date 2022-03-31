


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
    
    '''
    m = [n]  # 4,2,1 loop

    for i in range(2):
        # first 3 elements of the loop
        n = f(n)
        m.append(n)
        # print(m)

    for i in range(2, 10000):
        # all the other loops
        n = f(n)
        # print(n)
        m.pop(0)
        m.append(n)
        # print(m)
        if m == [4,2,1]:
            return i
            

d = {}
for n in range(10_000):
    # n = 22  # initial number
    x = number_iterations(n)
    # print(n, x)
    d[n] = x

print(d.values())

# how many None's
print('number of nones', len([x for x in d.values() if x==None]) )
number_answers = [x for x in d.values() if x!=None]
print('max', max(number_answers))
print('avg', round(average(number_answers)))
print('std', round(std(number_answers)))

plt.plot(d.keys(), d.values())
plt.xlabel('number n')
plt.ylabel('number of iterations')
 
# giving a title to my graph
plt.title('Collatz Conjecture - iterations for n')
plt.show()

