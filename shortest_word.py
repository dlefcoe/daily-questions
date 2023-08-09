'''
given a sentance get the shortest word from the sentance.

The shortest word is x.
    => x

    words.split('The shortest word is x.')
    [The, shortest, word, is, x]
    [3  , 8       , 4   , 4 , 1]

    {The:3, shortest:8, word:4, is:2    ....}

'''


import string


def main():

    # the first method
    s = 'The shortest word is x.'
    r = shortest_word(s)
    print('the first shortest word is:', r)

    # the second method
    sentence = "Hi there! This is a sample, sentence with punctuation."
    r = new_short_word(sentence)
    print('the new shortest word is:', r)


def shortest_word(s:str):
    ''' get shortest word '''

    # remove punctuation 
    translate = str.maketrans('', '', string.punctuation)
    words = s.translate(translate)

    words = {w:len(w) for w in words.split()}
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


