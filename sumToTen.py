'''
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.

completed by d ross: 2009_09_09

works.

'''

def ten(number):
    numberstr = str(number)
    total = sum(int(x) for x in numberstr)
    if total == 10:
        return number
    elif total < 10:
        return int(numberstr + str(10 - total))
    else:
        return "Input number has digits that sum to more than 10."

# TESTING
for x in [3, 6, 142, 53453, 15, 363]:
    print(x, "-->", ten(x))


