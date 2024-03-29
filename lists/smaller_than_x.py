# A function that takes an array and a given x,
# that returns a list with all numbers strictly
# smaller than x. P.s. nice syntax.

def smaller_than_x(arr, x):
    l = [i for i in arr if i < x]
    return l

l = [1, 2, 7, 9, 10]
x = 9
print(smaller_than_x(l, x))

# Same as above except returns all numbers
# strictly greater than x.
def greater_than_x(arr, x):
    l = [i for i in arr if i > x]
    return l
print(greater_than_x(l, x))