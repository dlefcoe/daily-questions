'''
This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.

'''



'''
initial thoughts

possible directions:
'''
import math


# these are the possible directions split horizontally and vertically
possibleDirections = {'N':(1,0), 'S':(-1,0), 'E':(0,1), 'W':(0,-1),}


'''
here is the rule for decoding:

A NW B
=> a = b + n + w
=> a = b + (1,0) + (0,-1)
=> a = b + (1,-1)


B NE C
=> b = c + n + e
=> b = c + (1,0) + (0,1)
=> b = c + (1,1) 
'''


def decodeDirection(point1, direction, point2):
    ''' get point1 = point2 + [i,j]
    inputs:
    point1: a letter (type string)
    point2: a letter (type string)
    direction: a string (of one char or 2 chars)

    output:
    point1: a letter (type string)
    point2: a letter (type string)
    direction: an array [i,j]
    
    '''

    v = [0,0]
    for i in direction:
        # get value from dict
        move = possibleDirections.get(i)
        
        v[0] = v[0] + move[0]
        v[1] = v[1] + move[1] 

    # something like A(i,j) = B(i,j) + Move(i,j)
    return point1, v, point2



def breakIntoThreeParts(rule):
    point1 = rule[0]
    point2 = rule[-1]
    if len(rule) == 5:
        move = rule[2]
    elif len(rule) == 6:
        move = rule[2:4]


    return point1, move, point2


'''
...good code here, but dont need....
r = 'A NW B' #len 6 rule
tp = breakIntoThreeParts(r)
# parse rule into decoder
out = decodeDirection(*tp)
print(out)

r = 'A W C' # len 5 rule
tp = breakIntoThreeParts(r)
# parse rule into decoder
out = decodeDirection(*tp)
print(out)
'''

# code to test decodeDirection()
# yay = decodeDirection('A', 'ne', 'B')
# print(yay)



def workOnRuleList(ruleList):
    ''' Takes the list of rules (as a list of strings) '''

    out = [] #output list
    for i in ruleList:
        tp = breakIntoThreeParts(i)
        out.append(decodeDirection(*tp))
    #print(out)    

    # test verticals
    for i in out:
        print('point1:', i[0], ', point2:',i[2], ', Vertical move vector:', i[1][0])  

    # test horizontals
    for i in out:
        print('point1:', i[0], ', point2:',i[2], ', Horizontal move vector:', i[1][1])  

    return True


print('--- work on the rule list ---')
ruleList = ['A N B', 'B NE C', 'C N A']
workOnRuleList(ruleList)



