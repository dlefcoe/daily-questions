'''

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list.
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

'''


s = [12, 1, 61, 5, 9, 2]
k = 24



def subsetSum(arr, tgt):
    arr.sort(reverse=True)

    # throw out big numbers
    for i, val in enumerate(arr):
        if val > tgt:
            arr.pop(i)

    # find sequence that works
    
    # start with biggest numer
    g = 0
    newList = []
    for i, val in enumerate(arr):
        
        if g + val > k:
            # the number is too big
            pass
        elif g + val == k:
            # correct number and finish
            newList.append(val)
        else:
            # the number is too low, so include and continue
            g = g + val
            newList.append(val)


    return newList


print(subsetSum(s, k))



