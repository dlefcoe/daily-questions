'''

Given a real number n, find the square root of n. For example, given n = 9, return 3.


'''



def main():
    ''' the main routine '''    
    n = input('enter a number: ')
    answer = squareRoot(n)
    print(answer)

    print('invoking second method')
    rossSquareRoot(n)


def squareRoot(n):
    ''' square root of a number by iteration 
    
    parameters:
        n: number to find square root of

    return:
        nOut: the square root of n
    '''

    n = float(n)
    if n == 1:
        return 1


    if n < 1:
        # make logical start guess for n < 1
        guess = 2*n

        for _ in range(1, 21):
            if guess*guess > n:
                guess = guess * 1.1
            elif guess*guess < n:
                guess = guess * 0.9
            else:
                return guess



        for _ in range(1, 21):
            if guess*guess > n:
                guess = guess * 1.01
            elif guess*guess < n:
                guess = guess * 0.99
            else:
                return guess



        for _ in range(1, 101):
            if guess*guess > n:
                guess *= 1.001
            elif guess*guess < n:
                guess *= 0.999
            else:
                return guess

        return guess



    # make a logical start guess for n > 1
    guess = 0.1 * n

    print('...first batch working...')
    for i in range(1, 21):
        # do process 100 times
        if guess*guess > n:
            #print(f'{guess} is too large {i}')
            guess = 0.9*guess
        elif guess*guess < n:
           # print(f'{guess} is to small {i}')
            guess = 1.1*guess
        else:
            #print(f'{guess} is correct {i}')
            return guess
        
    print('...second batch working...')
    for j in range(1, 21):
        # do process 100 times
        if guess*guess > n:
            #print(f'{guess} is too large {i} - {j}')
            guess = 0.99*guess
        elif guess*guess < n:
            #print(f'{guess} is to small  {i} - {j}')
            guess = 1.01*guess
        else:
            #print(f'{guess} is correct  {i} - {j}')
            return guess

    print('...third batch working...')
    for k in range(1, 21):
        # do process 100 times
        if guess*guess > n:
            #print(f'{guess} is too large  {i} - {j} - {k}')
            guess = 0.999*guess
        elif guess*guess < n:
            #print(f'{guess} is to small {i} - {j} - {k}')
            guess = 1.001*guess
        else:
            #print(f'{guess} is correct {i} - {j} - {k}')
            return guess


    return guess




def rossSquareRoot(n):
    
    n = float(n)
    goal = n
    iterations = 15
    lower = 0
    upper = goal

    if n < 1:
        upper = 1

    for _ in range(iterations):

        attempt = (lower + upper) / 2

        if attempt * attempt < goal:
            lower = attempt
        else:
            upper = attempt

        print(attempt)



if __name__ == "__main__":
    main()
    pass