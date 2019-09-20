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

    # if compToLast(arr) == False:
    #     print(arr)
    #     return False

    if compareToRemain(arr) == False:
        print(arr)
        return False

    # if compareToBegin(arr) == False:
    #     print(arr)
    #     return False

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

def compareToBegin(arr):
    ''' compare to begining of the list '''
    badCount = 0
    for i, val in enumerate(reversed(arr)):
        if val < max(arr[i:]):
            badCount += 1
            if badCount > 1:
                return False
    return True        


def nonDecrease(arr):
    ''' compare elements of array to make sure increasing '''
    print(arr)
    
    for i, val in enumerate(arr):
        if i != 0:
            # dont process first element

            if val < arr[i-1]:
                # either arr[i] is too small or arr[i-1] is too large
                
                # remember point of failure
                indexToRestore = i-1
                valToRestore = arr[i-1]

                # now decrease arr[i-1] to a working value
                arr[i-1] = arr[i]
                # and check if this works now
                for j, val in enumerate(arr):
                    if j != 0:
                        # start at j = 1
                        if val < arr[j-1]:
                            # this did not help, so restore the values
                            arr[indexToRestore] = valToRestore

                            # now increase arr[i] and check
                            arr[i] = arr[i-1]
                            for k, val in enumerate(arr[1:]):
                                if k != 0:
                                    # start at k = 1
                                    if val < arr[k-1]:
                                        # failed again
                                        return False
                            return True
                return True
    return True


            




arr = [0,0,0,0,0,0,0]
# print(testarray(arr))
print(nonDecrease(arr))

arr = [0,0,0,1,0,0,0]
print(nonDecrease(arr))

arr = [10, 5, 7]
print(nonDecrease(arr))


arr = [10, 5, 12]
print(nonDecrease(arr))

arr = [12, 5, 2]
print(nonDecrease(arr))

arr = [0,0,0,1,2,0,0,0]
print(nonDecrease(arr))

arr = [1,2,1,2,1,2,1,2]
print(nonDecrease(arr))

arr = [1,2,3,1,2,3]
print(nonDecrease(arr))

arr = [1, 2, 0, 1]
print(nonDecrease(arr))

arr = [1, 2, 5, 1]
print(nonDecrease(arr))


# bad = [10, 5, 1]  
# good = [1, 10, 6, 10, 6, 100]
# good = [0, 1, 1, 1, 0, 0]

# print(deltaMethod(arr))
