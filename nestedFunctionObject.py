'''


This problem was asked by Jane Street.
cons(a, b) constructs a pair, and car(pair) and cdr(pair)returns the first and last element of that pair.
For example, car(cons(3, 4))returns 3, and cdr(cons(3, 4))returns 4.

Given this implementation of cons:

def cons(a, b): 
    def pair(f): 
        return f(a, b) 
        return pair 

Implement car and cdr.


'''


def cons(a, b):
    def pair(f):
        return f(a, b)
#    def f(a,b):
#        return a + b
    return pair

# ref to the function
print(cons(2,5))

def car(somepair):
    def getfirst(a,b):
        return a
    return somepair(getfirst)

def cdr(somepair):
    def getsecond(a,b):
        return b
    return somepair(getsecond)


print(car(cons(3,4)))
print(cdr(cons(3,4)))




''' completed by d ross '''