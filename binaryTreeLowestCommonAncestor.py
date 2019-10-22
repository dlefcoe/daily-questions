'''

This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. 
Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants 
(where we allow a node to be a descendant of itself).”


'''


# A Python class that represents an individual node  
# in a Binary Tree 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        





# Compute the "maxDepth" of a tree -- the number of nodes  
# along the longest path from the root node down to the  
# farthest leaf node 
def maxDepth(node):
    global counter
    counter += 1
    if node is None: 
        return 0 ;  
  
    else : 
  
        # Compute the depth of each subtree 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right)

        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1



# create root 
root = Node(1) 
''' following is the tree after above statement 
        1 
      /   \ 
     None  None'''


root.left      = Node(2); 
root.right     = Node(3); 
    
''' 2 and 3 become left and right children of 1 
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   None None None None'''


root.left.left  = Node(4); 
'''4 becomes left child of 2 
           1 
       /       \ 
      2          3 
    /   \       /  \ 
   4    None  None  None 
  /  \ 
None None'''   




print(root.left.left.val)


counter = 0
print(f'the height of the tree is {maxDepth(root)}')


print(f'counter counts: {counter}')
