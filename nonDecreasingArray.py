'''

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

'''



def testarray(arr):
    ''' check to see if array is not decreasing 

    prints final array and returns True or False
    '''

    if compToLast(arr) == False:
        print(arr)
        return False

    if compareToRemain(arr) == False:
        print(arr)
        return False

    badcount = 0

    if len(arr) <= 2:
        #fakkin simple
        return True

    if arr[-2] > arr[-1]:
        badcount +=1

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


def deltaMethod(arr):
    ''' check the sum of the slopes > 0 '''
    delta = []

    for i, val in enumerate(arr[1:]):
        delta.append(arr[i+1]-arr[i])

    #print(arr)
    #print(delta)
    print('sum of delta:', sum(delta))
    if sum(delta) < 0:
        #sloping down
        return False
    return True



def compToLast(arr):
    ''' compare all elements to the last one'''
    badCount = 0
    for i in arr:
        if i > arr[-1]:
            badCount += 1
            if badCount >1:
                return False
    


    return True

def compareToRemain(arr):
    ''' compare to remainder of the list '''
    badCount = 0
    for i, val in enumerate(arr):
        if val > min(arr[i:]):
            badCount += 1
            if badCount > 1:
                return False
    return True
        

arr = [0,0,0,0,0,0,0]
print(testarray(arr))

arr = [0,0,0,1,0,0,0]
print(testarray(arr))

arr = [10, 5, 7]
print(testarray(arr))

arr = [10, 5, 12]
print(testarray(arr))

arr = [12, 5, 2]
print(testarray(arr))

arr = [0,0,0,1,2,0,0,0]
print(testarray(arr))

arr = [1,2,1,2,1,2,1,2]
print(testarray(arr))

arr = [1,2,3,1,2,3]
print(testarray(arr))

arr = [1, 2, 0, 1]
print(testarray(arr))

# bad = [10, 5, 1]
# good = [1, 10, 6, 10, 6, 100]
# good = [0, 1, 1, 1, 0, 0]

# print(deltaMethod(arr))
