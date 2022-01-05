l1 = [1, 3, 4, 2, 5]
dict1 = {x:x**3 for x in l1}
print(dict1)

d2 = {x:f"ID{x}" for x in range(5)}
print(d2)

l2 = [101, 103, 102]
l3 = ['gfg', 'ide', 'greenus']

d3 = {l2[i]:l3[i] for i in range(len(l2))}
print(d3)