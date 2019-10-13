'''


This problem was asked by Square.
Given a string and a set of characters, return the shortest substring containing all the characters in the set.
For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".
If there is no substring containing all the characters in the set, return null.


my question:  do we assume that the set of characters appears in the same order in the string ?

'''

# this is a more general method
def shortFind(s, c):
    '''
    inputs:
    s: type=string, represents the string to test
    c: type=string, represents the list to find within the string

    return:
    sOut: type=string (or null) depending on s and c 

    '''



    return



# this works if the letters within c occur in the same order in the string s.
# as set out in the question above.
def shortSubstring(s, c):
    '''
    inputs:
    s: type=string, represents the string to test
    c: type=string, represents the list to find within the string

    return:
    sOut: type=string (or null) depending on s and c 

    '''

    # the most obvious case
    if c in s:
        sOut = c
        return sOut


    # check if all the letters of c exist in s
    for i in c:
        if i in s:
            sOut = 'all elements good'
            continue
        else:
            # no solution exists
            sOut = None
            return sOut

    # last index in s of first element in c
    lastIndex = 0
    for i, v in enumerate(s):
        if v == c[0]:
            lastIndex = i

    # first index in s of last element in c that occurs after the lastIndex above
    firstIndex = len(s)
    for i, v in enumerate(s[lastIndex:]):
        if v == c[-1]:
            firstIndex = i + lastIndex + 1
            break

    # print(lastIndex)
    # print(firstIndex)

    sOut = s[lastIndex:firstIndex]
    return sOut



s = 'figehaeci'
c = 'aei'
#c = [x for x in c]

answer = shortSubstring(s, c)
print(answer)












