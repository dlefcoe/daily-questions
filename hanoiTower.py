'''
The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

All the disks start off on the first rod in a stack. 
They are ordered by size, with the largest disk on the bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

You can only move one disk at a time.
A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
You cannot place a larger disk on top of a smaller disk.

Write a function that prints out all the steps necessary to complete the Tower of Hanoi. #
You should assume that the rods are numbered, with the first rod being 1, 
the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3


'''

import time as t



class counter: # object for counting
    moves = 0

def moveTower(height,fromPole, toPole, withPole):
    ''' recursive function for moving discs 
    
    The function ends once the height parameter condition is no longer satisfied
        (ie. the height of pole1 & pole2 = 0)
    ''' 
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    ''' increments the counter and prints the move '''
    counter.moves += 1
    print("moving disk from",fp,"to",tp)


h = int(input('enter a height (+ve integer): '))
start = t.time()
moveTower(h,"A","B","C")
print('number of moves:',counter.moves)
end = t.time()
print('time taken (sec):', round(end - start,2))



