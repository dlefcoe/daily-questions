'''

This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap

'''


class stackItem:
    ''' stack class '''

    def __init__(self, value):
        self.value = value
        self.n = False

    
    def push(self, item):
        ''' add item to the stack '''
        self.value = stackItem(item)
        self.n = True
        

    def pop(self):
        ''' remove last item from stack '''
        self.value = None
        if self.n == False:
            print('this is the last node')
        

        

def runMain():
    ''' this is the main routine '''

    # create stack
    s = stackItem(10)
    print(s.__dict__)

    # push to stack
    s.push(20)
    print(s.__dict__)
    print(s.value.__dict__)
    
    # remove last element from stack
    s.pop()
    print(s.__dict__)


if __name__ == "__main__":
    runMain()