'''

Given a mapping of digits to letters (as in a phone number), and a digit string, 
return all possible letters the number could represent.

You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} 
then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].


Year: 2009
Author: Darren

'''


import itertools




def poss(s, mapp):
    '''
    take a number input as a string: s
    take a dictionary(object): mapp

    return a list (array) of all possible outcomes
    '''

    # list of lists from the dict
    Lst = [mapp[x] for x in list(s)]
    
    print('here are the lists:')
    print(Lst)

    print('\nhere are the results:')
    result = itertools.product(*Lst)
    for i in result:
        print(i)

    print('--- all done ---')
    return True


s = '23'
mapp = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}
mapp = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i']}

poss(s, mapp)



