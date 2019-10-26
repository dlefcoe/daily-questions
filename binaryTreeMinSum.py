'''
by: Darren Lefcoe

Given a binary tree, return the level of the tree with minimum sum.

reference to code: 
https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/


example:
            10
        8           2
    3       5    2

paths:
10 -> 8 -> 3
10 -> 8 -> 5
10 -> 2 -> 2


'''


# binary tree node contains data field ,  
# left and right pointer 
class Node: 
    # constructor to create tree node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None



def printPaths(root): 
    '''function to print all path from root to leaf in binary tree '''
    # list to store path 
    path = []
    # list to store list of paths
    pathsList = []
    printPathsRec(root, path, 0, pathsList)     
    print(pathsList)

    # find the smallest
    smallest = min([sum(i) for i in pathsList])
    print(f'the smallest value is: {smallest}')

def printPathsRec(root, path, pathLen, pathsList): 
    ''' Helper function to print path from root to leaf in binary tree '''

    

    # Base condition - if binary tree is 
    # empty return 
    if root is None: 
        return
  
    # add current root's data into  
    # path_ar list 
      
    # if length of list is greater than path len 
    if(len(path) > pathLen):  
        path[pathLen] = root.data 
    else: 
        path.append(root.data) 
  
    # increment pathLen by 1 
    pathLen = pathLen + 1
  
    if root.left is None and root.right is None: 
          
        # leaf node then print the list 
        printArray(path, pathLen, pathsList)
    else: 
        # try for left and right subtree 
        printPathsRec(root.left, path, pathLen, pathsList) 
        printPathsRec(root.right, path, pathLen, pathsList) 


    
# def lowestValArray(ints, len):
#     ''' function to get the lowest path value '''



def printArray(ints, len, pathsList): 
    ''' Helper function to print list in which root-to-leaf path is stored '''
    print(ints, ' total =', sum(ints))
 
    pathsList.append(ints.copy())
    

# program to test the function

'''
binary tree example:

            10
        8           2
    3       5    2

'''

root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2) 
printPaths(root) 


