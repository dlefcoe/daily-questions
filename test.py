'''



'''



class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Print all nodes."""
        out = str(self.val)
        if self.next: out += str(self.next)
        return out


def swaptwo(node):
    """Swap two nodes."""
    # Swap value of two nodes
    if node and node.next:
        node.val, node.next.val = node.next.val, node.val

    # Repeat for the rest
        if node.next.next:
            swaptwo(node.next.next)

    return node


tree = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7) ))))))

print(tree)
swapped = swaptwo(tree)
print(swapped)