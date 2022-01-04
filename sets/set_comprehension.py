l = [10, 20, 3, 4, 10, 20, 7, 3]

s1 = {x for x in l if x % 2 == 0}
print(s1)
s2 = {x for x in l if x % 2 != 0}
print(s2)

print(type(s1))
print(type(s2))

my_set = {10, 20, 30}
print(type(my_set))

rando_dict = {i : 'cool' for i in s1}
print(type(rando_dict))