s = {10, 20, 30}
print(s)

s.add(40)
print(s)

# update with tuple
s.update((95, 94), (67, 68))
print(s)

#update with list
s.update([1, 4, 2])
print(s)

#update with set and list
s.update({42.5, 42.4}, [0, 13])
print(s)
print(type(s))