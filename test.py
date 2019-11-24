'''



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

tree = Node(1, Node(2, Node(3, Node(4))))

#     1 -> 2 -> 3 -> 4 -> 5 -> 6
#     2 -> 1 -> 4 -> 3 -> 6 -> 5

def swaptwo(node):
    """Swap two nodes. Return head"""
    a = node
    b = node.next
    c = node.next.next

    b.next = a
    a.next = c.next
    return b


print(tree)