'''


Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

'''


class Node:
    ''' class for a node '''

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    ''' class for single linked list '''

    def __init__(self):
        self.headval = None


    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
            
    
    def lengthList(self):
        ''' returns the length of the list '''

        emergencyBreak = 0
        counter = 0
        n = self.headval
        while n is not None:
            emergencyBreak += 1
            counter += 1
            n = n.nextval

            if emergencyBreak >= 1000:
                print('emergency break used')
                break
        return counter


    def swapValues(self):
        ''' swap the lavues in SLL '''
        n = self.headval

        # swap head value and first value
        val1 = n.dataval
        n = n.nextval
        

        counter = 0
        while n is not None:
            counter += 1
            n = n.nextval
            val2 = n.dataval
            
            pass

        pass



def code():
    ''' run the code '''

    # instance of list
    list1 = SLinkedList()

    # head of list
    list1.headval = Node(1)

    # nodes
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)
    e5 = Node(5)

    # Link first Node to second node
    list1.headval.nextval = e2

    # Link second Node to third node
    e2.nextval = e3

    # Link third Node to fourth node
    e3.nextval = e4

    e4.nextval = e5

    print('print the list')
    list1.listprint()

    # list length
    print('lenght of list: ', list1.lengthList())

    # if odd do not swap
    if list1.lengthList()%2 != 0:
        # odd, do no not swap
        print('the list is odd length, so cannot swap')
        # raise Exception(f'list length {list1.lengthList()} is odd. Needs to be even')        
    else:
        # even so can swap values
        list1.headval.dataval, e2.dataval = e2.dataval, list1.headval.dataval
        e3.dataval, e4.dataval = e4.dataval, e3.dataval
        print('print the swapped list')
        list1.listprint()

        # note we could sent the ei values to a list and traverse through the list, but this would be defeating the purpose of the list


    print('memory size of singly linked list:',list1.__sizeof__())
    print(list1.__dict__)
    print(e2.__dict__)



# main routine
if __name__ == "__main__":
    code()
