l = [10, 20, 3, 4, 10, 20, 7, 3]

s1 = {x for x in l if x % 2 == 0}
print(s1)
s2 = {x for x in l if x % 2 != 0}
print(s2)