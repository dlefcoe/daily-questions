

'''

The Collatz Conjecture is the simplest math problem no one can solve 
— it is easy enough for almost anyone to understand but notoriously 
difficult to solve.


'''


def f(n):
    if n % 2 == 0:
        # have an even number
        v = int(n/2)
        return v
    if n%2 !=0:
        # have an odd number
        v = n * 3 + 1
        return v


n = 20  # initial number
m = [n]  # 4,2,1 loop

for i in range(2):
    # first 3 elements of the loop
    n = f(n)
    m.append(n)
    print(m)

for i in range(2, 100):
    # all the other loops
    n = f(n)
    # print(n)
    m.pop(0)
    m.append(n)
    print(m)
    if m == [4,2,1]:
        print('finished at', i)
        break
