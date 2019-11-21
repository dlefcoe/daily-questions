'''


Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].


'''

import numpy as np



def partList(x, LLL):
    ''' partition list at value = x '''

    nList = np.array(LLL)

    # position of x in list
    pos = np.where(nList == x)
    pos = pos[0][0]

    newList = np.partition(nList, pos)
    return newList



# run the code
if __name__ == "__main__":
    
    x, l = 10, [9, 12, 3, 5, 14, 10, 10]    
    a = partList(x, l)
    print(a)

