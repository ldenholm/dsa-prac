def factorial(n):
    assert n is int and n >= 0, 'number must be a positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n -1) 
    

print(factorial(-1))