'''


This problem was asked by Google.

Given two non-empty binary trees s and t, 
check whether tree t has exactly the same structure and node values with a subtree of s. 

A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself.


'''


# A Python class that represents an individual node  
# in a Binary Tree 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

# create roots for 2 different trees
s = Node(1)
t = Node(1)

#create nodes for s
s.left = Node(2)
s.right = Node(3) 


s.left.left  = Node(4)
'''4 becomes left child of 2 
           1 
       /       \ 
      2          3 
    /   \       /  \ 
   4    None  None  None 
  /  \ 
None None'''   

#create nodes for t
t.left = Node(2)
t.right = Node(3) 


t.left.left  = Node(3)







def compareBinTree(s, t):
    ''' compare two binary trees, s & t
    
    if they match, return true
    if they do not match, return false

    '''

    # perform comparison
    if s.val == t.val:
        print('roots are the same')
        res = True
    else:
        print('unequal roots')
        res = False
    
    # check for left nodes
    if s.left and t.left:
        print('s.left and t.left exists')
        if s.left.val == t.left.val: # check if values are equal
            print('left nodes match')
            res = True
            # work on left subtree recursively
            compareBinTree(s.left,t.left)
        else:
            print(f'{s.left.val} is not equal to {t.left.val}')
            res = False
            return res
    
    if not s.left and not t.left:
        print('s.left and t.left both do not exits')
        res = True
    
    if (not s.left and t.left) or (s.left and not t.left):
        print('s and t do not match, s = {s.left}, t = {t.left}')
        res = False
        return res
    

    # check for right nodes
    if s.right and t.right:
        print('s.right and t.right exists')
        if s.right.val == t.right.val: # check if values are equal
            print('right nodes match')
            res = True
            # work on right subtree recursively
            compareBinTree(s.right,t.right)
        else:
            print(f'{s.right.val} is not equal to {t.right.val}')
            res = False
            return res
    
    if not s.right and not t.right:
        print('s.right and t.right both do not exits')
        res = True
    
    if (not s.right and t.right) or (s.right and not t.right):
        print('s and t do not match, s = {s.right}, t = {t.right}')
        res = False
        return res


    return res


r = compareBinTree(s, t)
print(r)

