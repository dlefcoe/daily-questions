'''

This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.


'''

def main():
    ''' the main code (no inputs or returns) '''
    array = [[1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1]]
    
    answer = largestRectangle(array)
    print('the largest value:',answer)



def largestRectangleMethod1(a):
    '''  find the largest rectangle containing only 1's and return its area 
    
    parameters:
        a: array of bool's

    return:
        area: integer representing area

    '''

    # is there a side neighbour
    for i in a:
        for j in range(len(i)):
            if j == 0: continue
            if i[j] == 1 and i[j-1] == 0:
                print('have a side neighbour')
    
    # is there a vertical neighbour
    for i in range(len(a)):
        if i == 0: continue
        for j in range(len(a[0])):
            if a[i][j] == 1 and a[i-1][j] == 1:
                print('have a vertical neighbour')


    
    return 100

# have just realised
# can scan a[i][j] for i in range(len(a)-1), for j in range(len(a)-1)

# also, might be able to use itertools ?

# also, does numpy have inbuilt for this already ?

def largestRectangle(a):
    '''  find the largest rectangle containing only 1's and return its area 
    
    parameters:
        a: array of bool's

    return:
        area: integer representing area

    '''

    # build array for values
    maxRect = [[0 for i in range(len(a[0])-1)] for j in range(len(a)-1) ]
    

    for i in range(len(a)-1):
        for j in range(len(a[0])-1):
            # now do some processing.
            # print(a[i][j])

            if a[i][j]==1:
                maxRect[i][j] = 1
                # build a rectangle across

                # area to test
                # if extendRight([a[j] for row in a[0:i]]):
                #     maxRect[i+1][j] = 1
                moveX = 0
                while a[i][j+ moveX] == 1 and j+moveX < len(a[0])-1:
                    moveX += 1
                    maxRect[i][j] += 1
                    print('x across', moveX, ' at position down:across',i, j)
                    
                    moveY = 0
                    while a[i+moveY][j] == 1 and i+moveY < len(a)-1:
                        moveY += 1
                        maxRect[i][j] += 1
                    print('y down', moveY, ' at position down:across',i, j)
                
                '''
                if a[i+1][j] == 1:
                    maxRect[i][j] += 1
                    if a[i][j+1] == 1 and a[i+1][j+1] == 1:
                        maxRect[i][j] += 2
                '''


    print('this is the max rect:')
    print(maxRect)


    # there are 3 builds
    # horizontal, vertical, h+v

    # restricted to extendLeft() and extendDown() -> binary tree


    # return the largest value
    largestValue = 0
    for i in maxRect:
        for j in i:
            if j > largestValue:
                largestValue = j

    return largestValue


##
# an array is extendable leftwards if all the elements on the LHS are = 1 
##



def extendRight(m):
    ''' given a matrix (m = h*w), can it extend left 
    
    parameters:
        a: matrix of bool

    return:
        bool, true if extendable, false otherwise
    '''
    extendable = False

    height = len(m)
    width = len(m[0])-1
    for i in range(height):
        if m[i][width] == 1:
            extendable = True
        else:
            extendable = False
            return False
    return extendable


    


def extendDown():
    ''' given a matrix, can it extend left '''
    pass



if __name__ == "__main__":
    main()

