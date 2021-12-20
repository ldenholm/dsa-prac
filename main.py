def factorial(n):
    assert n >= 0 and int(n) == n, 'number must be a positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n -1) 
    
def fibo(n):
    assert n >= 0 and int(n) == n, "number must be a positive int"
    # base case, use 0 and 1
    if n in [0, 1]:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

#print(factorial(-1))
print(fibo(5))
print(factorial(10))