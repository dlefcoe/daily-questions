
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



def testPalindrome(inList):
    dll = DoubleLinkedList()
    # create the double linked list
    for i in inList:
        dll.append(i)

    # here is the list
    dll.printList()

    print('the head:')
    print(dll.head.next)


    # check for head
    if dll.head.next:
        x = dll.head
        counter = 1
        while x.next:
            x = x.next
            counter += 1

    
    print('length of the double linked list:', counter)
    print('current value:', x.data)
    # go to the end of the double linked list and iterate backwards and compare to iteration forwards.
    for i in range(counter):
        continue


    return



inputDLL = [1, 4, 3, 4, 1]
testPalindrome(inputDLL)



'''
dll = DoubleLinkedList()
dll.prepend(0)
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.prepend(5)

dll.printList()
'''
