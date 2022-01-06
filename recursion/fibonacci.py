def fibonacci(n):
    # base case
    if n in [0, 1]:
        return n
    return n + fibonacci(n-1)


# input 3
# output 6
print(fibonacci(3))