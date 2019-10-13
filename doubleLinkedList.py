
'''

double linked list.

looks like this:
null  <- prev - [data]  <- prev - [data]  <- prev - [data] <- prev - null
      - next -> [  1 ]  - next -> [  2 ]  - next -> [  3 ] - next ->





'''



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.prev = None
            self.head = newNode
        else:
            newNode = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur
            newNode.next = None
    
    def prepend(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.prev = None
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


dll = DoubleLinkedList()
dll.prepend(0)
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.prepend(5)

dll.printList()
