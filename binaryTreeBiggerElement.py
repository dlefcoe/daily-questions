'''

This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.


'''



class Node:
    ''' node is created 
    
    parameters:
        parent: bool, exists if the node has a parent
        val: float, is the value
        left: is the value of the left (if None, there is no value)
        right: is the value of the right (if None, there is no value)
    
    Output:
        a new Node is created
    '''

    def __init__(self, parent, val, left, right):
        self.parent = parent
        self.val = val
        self.left = left
        self.right = right

        # parent is a bool
        if parent != True:
            parent = False

    


def runCode():

    # the top node
    x = Node(False, 10, Node(True, 5, None, None ), Node(True, 30, Node(True, 22, None, Node), Node(True, 35, None, None)))

    print(x.__dict__)
    print(x.left.val)
    print(x.right.val)
    print(x.right.right.__dict__)
    print(type(x.right.right))
    print(type(x.right.right.right))

    # create a new node
    x.right.right = Node(True, 100, None, 101)
    print(x.right.right.right)
    print(x.right.right.left)
    print(x.right.right)
    print(x.right.right.__dict__)
    x.right.right.right = Node(True, 101, None, None)
    print(type(x.right.right.right))
    print(type(x.right.right))
    # x = x.Node

    # how to get the value of the parent
    z = {"hello"+str(i):i for i in range(20)}
    print(z)


if __name__ == "__main__":
    runCode()

