'''

factorial recursively or iteratively


'''



def factRecursive(n, v=1):
    ''' take vaue n and return the factorial '''


    if n > 1:
        v = n * v
        return factRecursive(n-1, v)
    else:
        v = n * v
        return v


a = factRecursive(5)
print(a)



def recur_factorial(n):
    ''' better version '''  
    if n == 1:  
        return n  
    else:  
        return n*recur_factorial(n-1)




