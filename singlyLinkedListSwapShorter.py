'''


Given the head of a singly linked list, swap every two nodes and return its head.
For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

'''



class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


    def __repr__(self):
        """Print all nodes."""
        out = str(self.val)

        if self.next:
            out += str(self.next)

        return out

    def doSwap(self):
        ''' swap nodes '''
        a = self
        b = self.next

        if a and b:
            a.val, b.val = b.val, a.val

            # check the next
            c = self.next.next
            if c:
                c.doSwap()
                
        return b


    def lengthList(self):
        a = self
        count = 0
        
        while a is not None:
            # traverse list
            count += 1
            a = a.next

        print('length of list: ', count)
        return count

        



def runCode():


    tree = Node(1, Node(2, Node(3, Node(4))))

    #     1 -> 2 -> 3 -> 4 -> 5 -> 6
    #     2 -> 1 -> 4 -> 3 -> 6 -> 5

    print('original list:', tree)
    tree.doSwap()
    tree.lengthList()
    print('swapped list:', tree)





# this code does not get run #
def swaptwo(node):
    """Swap two nodes. Return head"""
    a = node
    b = node.next
    c = node.next.next

    b.next = a
    a.next = c.next
    return b




if __name__ == "__main__":
    runCode()

    