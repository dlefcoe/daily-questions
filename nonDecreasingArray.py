'''

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

'''



def testarray(arr):

    badcount = 0
    prev = arr[0]

    for i, cur in enumerate(arr[1:]):

        if cur < prev:
            badcount += 1
            arr[i+1] = prev
        
        prev = arr[i+1]

        if badcount > 1:
            return False

    return True

good = [10, 5, 7]
bad = [10, 5, 1]
good = [1, 10, 6, 10, 6, 100]
good = [0, 1, 1, 1, 0, 0]
print("Should get True, False..")
print(testarray(good), testarray(bad))

