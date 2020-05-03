'''

Testing wikipedia module in python

by: @dlefcoe

'''



import wikipedia
import time


t0 = time.time()
def wikiThings():
    t1 = time.time()
    w = wikipedia.summary('wikipedia')

    #print(w)
    print(type(w))

    t2 = time.time()

    print(f'time taken is {round(t2-t1, 3)} seconds')


    w = wikipedia.search('wikipedia')
    print(w)

    t3 = time.time()
    print(f'time taken is {round(t3-t2, 3)} seconds')

    w = wikipedia.page('world population')
    print(w)

    t4 = time.time()
    print(f'time taken is {round(t4-t3, 3)} seconds')



wikiThings()

