'''

This problem was asked by Facebook.
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations.
You can assume b can only be 1 or 0.


'''



def bitWise(x, y, b):

    r = (x * b) + (y * (b^1))

    return r

x = 10
y = 6

print(f'should print {y}:')
print(bitWise(x, y, 0))
print(f'should print {x}:')
print(bitWise(x, y, 1))
