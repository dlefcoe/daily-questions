"""

This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.

"""




l1 = [-10, -10, 5, 2]
l2 = [-10, -10, 5, 2, 15, 100]
lNeg = [-10, -10, -5, -2]
l3 = [1, 2, 3]
lOnePos = [-10, -5, -2, -8, 3]


def doProblem(l):
    """Take a list and work on it."""
    
    l = list(l)
    l.sort()

    # if the list is of len = 3, there are no options
    if len(l) == 3:
        print('list is len == 3, so answer =', l[0] * l[1] * l[2])
        return l[0] * l[1] * l[2]

    # different cases

    # determine number of positives
    posList = [x for x in l if x > 0]
    nPositives = len(posList)
    
    # determine number of negatives
    negList = [x for x in l if x < 0]
    nNegatives = len(negList)


    # 3 (or more) positives
    if nPositives >= 3:
        # highest 3 positives
        highest3 = posList[-3:]
        

        if nNegatives >= 2:
            # get the highest 2 negatives
            highestNegs = negList[:2]
            
            
            # are the highest 2 negatives > the lowest of the 3 positives
            if highestNegs[0] * highestNegs[1] > highest3[0] * highest3[1]:
                # if so, use them
                print('3 or more positives:', highestNegs[0] * highestNegs[1] * highest3[2])
                return highestNegs[0] * highestNegs[1] * highest3[2]
            else:
                # otherwise use highest 3 positives
                print('3 or more positives:', highest3[0] * highest3[1] * highest3[2])
                return highest3[0] * highest3[1] * highest3[2]
        
    


    # 1 or 2 positives
    if nPositives == 2 or nPositives == 1:
        # get the highest 2 negatives
        highestNegs = negList[:2]
        # get the highest positive
        p = posList[-1]
        # return the product
        print('1 or 2 positives, so answer =', highestNegs[0] * highestNegs[1] * p)
        return highestNegs[0] * highestNegs[1] * p




    # 0 positive (all negative list)
    if nPositives == 0:
        # get the lowest 3 values
        print('no positives, so:', l[-1] * l[-2] * l[-3])
        return l[-1] * l[-2] * l[-3]


    return True


doProblem(l1)
doProblem(l2)
doProblem(lNeg)
doProblem(l3)
doProblem(lOnePos)

