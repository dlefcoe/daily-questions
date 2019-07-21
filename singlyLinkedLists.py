'''

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

'''



listA = [3, 6, 9, 12]
listB = [99, 1, 4, 7, 8, 10, 12, 15, 18]


def firstFunction(listA, listB):
    # this function does O(m*n) time

    for i, val1 in enumerate(listA):
        for j, val2 in enumerate(listB):
            if val1 == val2:
                # we have a match
                print(f'the match value is: {val1}')
                print(f'the match index is: {i} and {j}')


def secondFunction(listA, listB):
    # try a faster method

    # first guess is in the middle of list A
    na = int(len(listA) / 2)
    fga =listA[na]
    print(na, fga)

    # get the middle of list B
    nb = int(len(listB) / 2)
    fgb = listB[nb]
    print(nb, fgb)

    # compate the values from list A and list B
    if fga == fgb:
        # we have a match
        print(f'element {na} from list A and element {nb} from list B and value {fga}')
        return fga

    
    while fga > fgb:
        # the value in list A was too high
        na -= 1
        fga = listA[na]
        print(fga)
        if fga == fgb:
            # we have a match
            print(f'element {na} from list A and element {nb} from list B and value {fga}')
            return fga


    while fga < fgb:
        # the value in list A was too low
        na += 1
        fga = listA[na]
        print(fga)   
        if fga == fgb:
            # we have a match
            print(f'element {na} from list A and element {nb} from list B and value {fga}')
            return fga


    while fga > fgb:
        # the value in list A was too high
        nb += 1
        fgb = listB[nb]
        print(fgb)
        if fga == fgb:
            # we have a match
            print(f'element {na} from list A and element {nb} from list B and value {fga}')
            return fga

    while fga < fgb:
        # the value in list A was too low
        nb -= 1
        fgb = listB[nb]
        print(fgb)   
        if fga == fgb:
            # we have a match
            print(f'element {na} from list A and element {nb} from list B and value {fga}')
            return fga




def compareValues(a, b):
    ''' take 2 values and compare '''
    if a == b:
        return a
    
    if a > b:
        # reduce b or increase a
        return 'a too high'
    
    if a < b:
        # reduce a or increase b
        return 'a too low'



if __name__ == "__main__":
    # firstFunction(listA, listB)
    secondFunction(listA, listB)    
    
