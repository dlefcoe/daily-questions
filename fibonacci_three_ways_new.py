###############
## Fibonacci ##
###############

# %%
import time as t

def main():
    ''' the main starting point of the code '''
    
    n = 30

    # run brute force (contains recursive)
    # we cannot decorate recursive functions
    # because the decoator is called many time.
    # but we can wrap in into a no recursive function.
    print('running brute force')
    fib_brute(n)


    # Memoized
    print('running memoised')
    fib_memo(n)


    # tabulation method
    print('running tabulation')
    fib_tab(n)
    

    # test how to create a list of a certain length
    # tabletest()

    # proof that can add a bool and an int
    # x = bool_plus_int()
    # print(x)

    return


def time_it(func):
    ''' a decorator function to time functions '''
    def wrapper(*args, **kwargs):
        start_time = t.time()
        result = func(*args, **kwargs)
        end_time = t.time()
        print(f"The function {func.__name__} took {end_time - start_time} seconds to run.")
        print(f'the result is {result}')
        print('-----------')
        return result
    return wrapper


### Brute-Force (recursive)
@time_it
def fib_brute(n:int)->int:
    ''' brute force method '''
    def helper(n:int):
        ''' this helper is recursive '''
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return helper(n - 1) + helper(n - 2)
    return helper(n)



### Memoized
@time_it
def fib_memo(n:int):
    ''' memoised method '''
    memo = {0: 0, 1: 1}
 
    def helper(n):
        if n not in memo:
            memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]
 
    return helper(n)



 
### Tabulation
@time_it
def fib_tab(n: int):
    ''' tabulation method'''
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n - 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    table[-1] += table[-2]
    return table[-1]


def tabletest():
    ''' create a table of a certain length '''
    n = 10
    table = [0] * (n + 1)
    print(table)


def bool_plus_int():
    ''' function showing that user can add bool + int '''
    a = True
    b = 10
    c = 3*a + b
    print(type(a))
    print(type(b))
    return c



# main guard idiom
if __name__=='__main__':
    main()
