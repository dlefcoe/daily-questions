'''
get the shortest word from a sentance in Python.
'''


import string


def main():

    # the first method
    s = 'The shortest word is x'
    r = shortest_word(s)
    print(r)

    # the second method
    sentence = "Hi there! This is another sample, sentence with punctuation."
    r = new_short_word(sentence)
    print('the new shortest word is:', r)


def shortest_word(s:str):

    words = {w:len(w) for w in s.split()}
    min_key = next(k for k,v in words.items() if v==min(words.values()))

    return min_key


def new_short_word(sentence:str):
    ''' find shortest word '''
    
    # Remove punctuation 
    translate = str.maketrans('', '', string.punctuation)
    sentence_no_punct = sentence.translate(translate)

    # Split into words
    words = sentence_no_punct.split() 

    # Get shortest word
    shortest_word = min(words, key=len)

    return shortest_word





if __name__=='__main__':
    # run as the main program guard
    main()





