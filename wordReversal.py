'''

This problem was asked by Facebook.

Given a string and a set of delimiters, 
reverse the words in the string while maintaining the relative order of the delimiters. 

For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"


'''



def wordReverse(s, d):
    """ takes a string, s, and delimeter, d, and outputs a reversed string.
    
    arguments:
        s: string 
        d: string

    return:
        sOut: string
    """

    newSentence = []
    delOrder = []
    newWord = ''
    for i, v in enumerate(s):
        delimeterFound = False
        for val in d:
            if val == v:
                delimeterFound = True
                delOrder.append(val)
                break
                
        if delimeterFound == False:
            # add character to the new word
            newWord = newWord + v
        if delimeterFound == True:
            # delimeter hit
            newSentence.append(newWord)
            newWord = ''
        if i == len(s)-1:
            # end of the string
            newSentence.append(newWord)
            break

    newSentence.reverse()

    # turn array back into string
    sOut = ''
    for n, val in enumerate(newSentence):

        sOut = sOut + val + delOrder[n-1]
    # remove last character
    sOut = sOut[:-1]

    return sOut




sent = 'hello/world:here'
delimeter = '/:'
r = wordReverse(sent, delimeter)
print(r)



testCase = ['hello/world:here/', 'hello//world:here']
delimeter = '/'
for i in testCase:
    r = wordReverse(i, delimeter)
    print(r)



