def even_odd(list):
    even = []
    odd= []
    for i in list:
        if i % 2 == 0:
            # is even
            even.append(i)
        else:
            odd.append(i)
    return even, odd

eventest = [10, 41, 30, 15, 80]
secTest = [10, 11, 12, 16]
print(even_odd(eventest))
print(even_odd(secTest))