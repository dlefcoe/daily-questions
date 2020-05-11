'''
This problem was asked by Google.

In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.

@dlefcoe

'''

# # matrix is a Toeplitz matrix or not 
# N = 5
# M = 4
  

# Function to check if all elements present in 
# descending diagonal starting from position 
# (i, j) in the matrix are all same or not 
def checkDiagonal(mat, i, j):
    
    # matrix dimensions
    N = len(mat)
    M = len(mat[0])     

    res = mat[i][j] 
    i += 1
    j += 1
      
    while (i < N and j < M): 
          
        # mismatch found 
        if (mat[i][j] != res): 
            return False
              
        i += 1
        j += 1
  
    # we only reach here when all elements 
    # in given diagonal are same 
    return True
  
# Function to check whether given   
# matrix is a Toeplitz matrix or not 
def isToeplitz(mat):
    ''' check if matrix is Toeplitz
    
    input:
        mat: n*m matrix
    output:
        True or False

    '''
    # matrix dimensions
    N = len(mat)
    M = len(mat[0])     
      
    # do for each element in first row 
    for j in range(M): 
          
        # check descending diagonal starting from 
        # position (0, j) in the matrix 
        if not(checkDiagonal(mat, 0, j)): 
            return False
      
    # do for each element in first column 
    for i in range(1, N):  
          
        # check descending diagonal starting  
        # from position (i, 0) in the matrix 
        if not(checkDiagonal(mat, i, 0)): 
            return False
          
    return True



# Driver Code  
if __name__ == "__main__": 
          
    mat = [[6, 7, 8, 9], 
          [4, 6, 7, 8], 
          [1, 4, 6, 7], 
          [0, 1, 4, 6], 
          [2, 0, 1, 4]] 
  
    print(f'matrix shape: (rows, columns) =  ({len(mat)}, {len(mat[0])})')

    if(isToeplitz(mat)): 
        print("Matrix is a Toeplitz") 
    else: 
        print("Matrix is not a Toeplitz") 


