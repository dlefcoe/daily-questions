'''

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

'''



listA = [3, 6, 8]
listB = [99, 1, 4, 7, 8, 10]


def firstFunction(listA, listB):

    for i, val1 in enumerate(listA):
        for j, val2 in enumerate(listB):
            if val1 == val2:
                # we have a match
                print(f'the match value is: {val1}')
                print(f'the match index is: {i} and {j}')


    pass



if __name__ == "__main__":
    firstFunction(listA, listB)
    pass
    
