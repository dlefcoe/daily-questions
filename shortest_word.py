'''
get the shortest word from a sentance in Python.
'''


import string

s = 'The shortest word is x'

def shortest_word(s:str):

    words = {w:len(w) for w in s.split()}
    min_key = next(k for k,v in words.items() if v==min(words.values()))

    return min_key

r = shortest_word(s)
print(r)





sentence = "Hi there! This is another sample, sentence with punctuation."



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


r = new_short_word(sentence)
print('the new shortest word is:', r)



