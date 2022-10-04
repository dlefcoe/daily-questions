# %% integrate function

def integrate(f:callable, a:float, b:float) -> float:
    ''' given a function, work out the integral '''
    
    area = 0
    x = a
    parts = 100000
    for i in range(parts):
        dx = (b-a)/parts        
        y_0 = f(x)
        y_1 = f(x+dx)
        x = x+dx
        height = (y_1 + y_0)  /2
        area = area + (height*dx)
    return area

# example function to integrate
def f(x): return 3*x**3 + x**2 + 11

r = integrate(f, 0, 1)
print(r)
