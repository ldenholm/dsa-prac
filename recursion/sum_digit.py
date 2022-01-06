def sum_digit(n):
    #logging
    print('floor div = ', n//10)
    print('modulo = ', n % 10)
    # base case
    if n < 10:
        return n
    return sum_digit(n//10) + n % 10

# n = 253
# ans = 10

# 253//10 = 
print(253//10)
print(253//10 + 253 % 10)
print(253%10)
print(sum_digit(253))
print(sum_digit(224))
print(sum_digit(111))