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

s = [12, 5, 5, 4]
k = 14



def subsetSum(arr, tgt):
    # if it naturally fits
    if sum(arr) == k:
        return arr
    
    # if list is too small
    if len(arr) < 2:
        return None

    arr.sort(reverse=True)

    # throw out big numbers
    for i, val in enumerate(arr):
        if val > tgt:
            arr.pop(i)

    for j in range(len(arr)-1):

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
                return newList
            else:
                # the number is too low, so include and continue
                g = g + val
                newList.append(val)

            # if you have got to the end with no fit
            if i == len(arr)-1:
                arr.pop(0)
        

        



print(subsetSum(s, k))





