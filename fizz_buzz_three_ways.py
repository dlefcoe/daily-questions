'''
fizz buzz three ways in python
'''

# %%
import time

def main():
    ''' the main entry point '''

    t1 = time.time()
    
    print('classical method:')
    fizz_buzz(100)
    print('--------')

    print('list method:')
    r = fizz_buzz_list(100)
    for i, v in enumerate(r):
        print(f'{i} : {v}')
    print('--------')

    print('dict method:')
    r = fizz_buzz_dict(100)
    for k,v in r.items():
        print(f'{k} : {v}')
    print('--------')

    t2 = time.time()
    print('time taken:', round(t2-t1,5), 'seconds')
    
    return


def fizz_buzz(n:int):
    ''' a function to calc fizz and buzz '''

    for i in range(n):
        if i%3==0 and i%5==0: print('fizzbuzz')
        elif i%3==0: print('fizz')
        elif i%5==0: print('buzz')
        else: print(i)
    
    return


def fizz_buzz_list(n:int):
    ''' a function to calc fizz and buzz in a list '''

    fbl = []

    for i in range(n):
        if i%3==0 and i%5==0: fbl.append('fizzbuzz')
        elif i%3==0: fbl.append('fizz')
        elif i%5==0: fbl.append('buzz')
        else: fbl.append(i)

    return fbl


def fizz_buzz_dict(n:int):
    ''' a function to calc fizz and buzz '''

    fbl = {}

    for i in range(n):
        if i%3==0 and i%5==0: fbl[i] = 'fizzbuzz'
        elif i%3==0: fbl[i] = 'fizz'
        elif i%5==0: fbl[i] = 'buzz'
        else: fbl[i] = i

    return fbl


# main guard idiom
if __name__=='__main__':
    main()
