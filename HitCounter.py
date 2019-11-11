
'''

This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). 

It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?


'''

import time as t

start = t.time()

class HitCounter:
    
    def __init__(self):
        ''' records a hit that happened at timestamp '''
        self.timestamp = [t.time() - start]
        self.count = [0]
        pass
    
    def total(self):
        ''' returns the total number of hits recorded '''
        return len(self.count)

    def range(self, lower, upper):
        ''' returns the number of hits that occurred between timestamps lower and upper (inclusive) '''
        hitsInRange = [n for n in self.timestamp if n > lower and n < upper]
        
        return len(hitsInRange)

    def aHitOccurs(self):
        ''' a hit occurs and gets recorded '''
        self.timestamp.append(t.time() - start)
        self.count.append(len(self.count))


# initialise hitcouner
x = HitCounter()
print(x.__dict__)


# simulate some hits
x.aHitOccurs()
print(x.__dict__)

t.sleep(0.5)

x.aHitOccurs()
print(x.__dict__)


# the total
print('the total: ',x.total())

print('hits in range: ', x.range(0.2, 10))





