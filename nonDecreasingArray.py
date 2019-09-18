'''

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

'''



def testarray(arr):

    badcount = 0

    for i, curr in enumerate(arr[:-2]):

        if arr[i] > arr[i+1]:
            # we have an issue
            badcount += 1
            if arr[i] > arr[i+2]:
                #arr[i] is too high
                arr[i] = arr[i+1]
            if arr[i] < arr[i+2]:
                #arr[i] is fine, but arr[i+1] is too low
                arr[i+1] = arr[i]
        
        if badcount > 1:
            print(arr)
            return False
    
    print(arr)
    return True




arr = [10, 5, 7]
arr = [10, 5, 12]
arr = [12, 5]
# bad = [10, 5, 1]
# good = [1, 10, 6, 10, 6, 100]
# good = [0, 1, 1, 1, 0, 0]
print(testarray(arr))



