


'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.

'''

import string
alphbt = dict()
for index, letter in enumerate(string.ascii_lowercase):
   alphbt[letter] = index + 1

'''
# examples of printables
print(alphbt['a'])
print(alphbt['b'])
print(alphbt.keys())
print(alphbt.values())
'''



n = input('enter a number >>>')
numToEval = n
stringToEval = str(numToEval)

print('The number to evaluate: ' + stringToEval)
for l in stringToEval:
    print(l)



'''
remember 12 = 1, 2 = a, b or 12 = L
a and b will fall into the singles array
L will fall into the doubles array

121 = [1, 2, 1] or [1, 21] or [12, 1]
12895103 = 1, 12 

more efficient working backwards ?
3, 10, 5, 9, 8, [1, 2 or 12]

working forwards:
[1, 2 or 12], 8, 9, 5, 10, 3 = 13 combinations

'''



lttrList = list(stringToEval)
print(lttrList)
print('the length of the list is: ' + str(len(lttrList)))

dCount = 1 # how many decodes
dcReduce = 0 # reduce the decodes
for i, val in enumerate(lttrList):
   # print(i, val)
    if val == '1':
        print('1 detected')
        # make sure 1 is not the end of list
        if i < len(lttrList)-1:
            # a zero cannot be a pair
            if lttrList[i+1] != '0':
                print('a pair exists')
                dCount = dCount + 1
                # if 11 or 12 this overcounts
                if (lttrList[i+1] =='1') | (lttrList[i+1] =='2'):
                    dcReduce += 1
    elif val == '2':
        print('2 detected')
        # make sure 2 is not the end of list
        if i < len(lttrList)-1:
            # a zero cannot be a pair
            if lttrList[i+1] != '0':
                # 27, 28, 29 cannot be a pair
                if (lttrList[i+1] != '7') | (lttrList[i+1] != '8') | (lttrList[i+1] != '9'):
                    print('a pair exists')
                    dCount = dCount + 1
    else:
        print('>=3 detected')

dCount = dCount - dcReduce
print('number of outcomes:', dCount)
        
    
        

