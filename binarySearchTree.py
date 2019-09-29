'''

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, 
and satisfies the constraint that the key in the left child must be less 
than or equal to the root and the key in the right child must be greater than or equal to the root.

'''


import random as rnd


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def makeRight(self, r):
        self.right = Node(r)
        # condition that right node >= root
        if r < self.val:
            self.right = self.val

    def makeLeft(self, l):
        self.left = Node(l)
        # condition that left node <= root
        if l > self.val:
            self.left = self.val





# make binary tree

# root of tree
root = Node(100)


# left side
root.makeLeft(rnd.randint(0,200))
root.left.makeLeft(rnd.randint(0,200))
root.left.makeRight(rnd.randint(0,200))

'''
root.left = Node(90)
root.left.left = Node(80)
root.left.right = Node(95)
'''

# right side
root.right = Node(110)
root.right.right = Node(120)
root.right.left = Node(105)




'''
root.makeLeft(99)
root.makeRight(101)
'''


# print root of tree
print(root.val, root.left, root.right)

# print second (left) level of tree
print(root.left, root.left.left, root.left.right)

# print second (right) level of tree
print(root.right.val, root.right.left.val, root.right.right.val)




# now check the tree
