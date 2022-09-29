# %%  newton-raphson

def function(x):
    ''' function of x '''
    return x**2 - 2

def derivative(x):
    ''' derivative of f(x) '''
    return 2*x

def newton_raphson(xn, f, df):
    ''' take xn, a function and its derivative 
    return x(n+1)
    '''
    xn1 = xn - f(xn)/df(xn)
    return xn1

# initial guess
initial_guess = 1.5

for i in range(10):
    next_guess = newton_raphson(initial_guess, function, derivative)
    if ((initial_guess / next_guess) - 1) < 0.000_000_001:
        print(f'exit at loop {i} with result {next_guess}')
        break
    else:
        initial_guess = next_guess

# exit at loop 3 with result 1.4142135623730951
