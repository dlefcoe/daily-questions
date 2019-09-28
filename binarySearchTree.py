'''

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, 
and satisfies the constraint that the key in the left child must be less 
than or equal to the root and the key in the right child must be greater than or equal to the root.

'''



class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def makeRight(self, r):
        self.right = r
        # condition that right node >= root
        if r < self.val:
            self.right = self.val

    def makeLeft(self, l):
        self.left = l
        # condition that left node <= root
        if l > self.val:
            self.left = self.val



root = Node(100)

root.makeLeft(99)
root.makeRight(101)


print(root.val, root.left, root.right)



