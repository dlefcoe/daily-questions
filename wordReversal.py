'''

This problem was asked by Facebook.

Given a string and a set of delimiters, 
reverse the words in the string while maintaining the relative order of the delimiters. 

For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"


'''



def wordReverse(s, d):
    ''' takes a string, s and delimeter, d and outputs a reversed string
    inputs:
    s: string
    d: string

    return:
    output: string
    '''

    newSentence = []
    newWord = ''
    for i, v in enumerate(s):
        if v != d:
            # add character to the new word
            newWord = newWord + v
        if v == d:
            # delimeter hit
            newSentence.append(newWord)
            newWord = ''
        if i == len(s)-1:
            # end of the string
            newSentence.append(newWord)
            break
    
    newSentence.reverse()

    return newSentence


sent = 'hello/world:here'
delimeter = '/'
r = wordReverse(sent, delimeter)
print(r)





