'''

Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.

'''


def runCode():
    ''' main code '''

    aList = [1,2,3,4,5,6,7,8,9,10]
    i, j = 3, 6
    
    # initial number of lists
    nList = 3

    # condition for first list
    if i == 0:
        print('need one less list')
        nList = nList - 1
    else:
        firstList = aList[0:i]
    
    # condition for middle list
    middleList = aList[i:j]

    # condition for third list
    if j == len(aList)-1: # remember lists start from 0
        print('need one less list')
        nList = nList - 1
    else:
        thirdList = aList[j:len(aList)-1]

    print(len(aList)-1)

    print(firstList, middleList, thirdList)

    # reverse the middle list
    middleList.reverse()



    # recombine the lists
    answer = firstList + middleList + thirdList
    print(answer)
    




if __name__ == "__main__":
    runCode()