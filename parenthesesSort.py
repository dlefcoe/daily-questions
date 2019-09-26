'''

This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid
(i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. 
Given the string ")(", you should return 2, since we must remove all of them.

'''





def parenthesesSort(pString):
    '''
    Input: string containing parenthasis
    Output: Integer containing number to remove
    '''


    #counter the open parenthesis
    openParen = 0
    # counter for removals
    n = 0
    for i in pString:
        if i == "(":
            openParen += 1
        elif i == ")":
            openParen -= 1
            if openParen < 0:
                n += 1
                openParen = 0
        else:
            print('bad character inserted')

    
    # end of the string is now reached
    n = n + openParen


    return n


ps = "()())()"
n = parenthesesSort(ps)
print(n)



ps = ")("
n = parenthesesSort(ps)
print(n)




def stringEliminateMethod(p):
    '''
    input: string p
    output: integer of len p
    '''

    failSafe = 1000
    while "()" in p:
        p = p.replace("()","")
        failSafe -= 1
        if failSafe < 0:
            break


    return len(p)


ps = "()())()"
n = stringEliminateMethod(ps)
print(n)



ps = ")("
n = stringEliminateMethod(ps)
print(n)



