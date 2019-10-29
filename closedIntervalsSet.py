'''

This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. 
If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], 
one set of numbers that covers all these intervals is {3, 6}.


'''


def smallestSet(*intervals):
    ''' takes any number of intervals and returns the smallest interval that covers those '''

    # get the smallest max
    smallMax = min([a[1] for a in intervals])
    largeMin = max([a[0] for a in intervals])
    

    interval = sorted([smallMax, largeMin])

    return interval


# the original question
x = smallestSet([0, 3], [2, 6], [3, 4], [6, 9])
print(x)

x = smallestSet([0, 50], [55, 100])
print(x)

x = smallestSet([0, 50], [45, 100])
print(x)


# intervals within each other
x = smallestSet([0, 100], [2, 98])
print(x)

x = smallestSet([0, 100], [2, 98], [3, 97])
print(x)


# intervals of zero size
x = smallestSet([20, 20], [10, 15])
print(x)
