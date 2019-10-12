'''


This problem was asked by Lyft.
Given a list of integers and a number K, return which contiguous elements of the list sum to K.
For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.



'''


def contigElem(intList, sumReq):
    '''
    takes a list and searches contiuous elements until k is found.

    intList: type=list, list of integers
    sumReq: type=integer, the resultant sum that user requires

    returns: a list representing the contiguous string.
    '''


    
    miniList = []
    for i, v in enumerate(intList):
        for j in intList[i:]:
            miniList.append(j)
            if sum(miniList) == k:
                return miniList
            elif sum(miniList) > k:
                # too large, empty the minilist
                miniList.clear() 
                break
            else:
                # k not reached
                continue

        

    return None


intList = [1, 2, 3, 4, 5]
k = 12


answer = contigElem(intList, k)
print(answer)


