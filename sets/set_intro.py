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

#=====================================
# more operations on sets

# discard ignores membership
s.discard(42.5)
print(s)

# check for membership before calling remove
s.remove(42.4)
print(s)

s.clear()
print('empty?', s)

s.add(420)
print(s)

# EVEN MORE operations :D
print(20 in s)
print(420 in s)
print(len(s))

#=====================================
#=====================================

s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}

#   UNION
print(s1 | s2)
# or
print(s1.union(s2))

# INTERSECTION
print(s1 & s2)
print(s1.intersection(s2))

# MINUS (Difference)
print(s1.difference(s2))
print(s1 - s2)
# both print 8, 2, 4 cos 6 is in s2

# SYMMETRIC DIFFERENCE
# everything in a and b but NOT those in both
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s1 ^ s2)

# Disjoint (no common element)
s1 = {2, 4, 6, 8}
s2 = {4, 8}
print(s1.isdisjoint(s2))

# SUBSET
print(s2 <= s1)
print(s2.issubset(s1))

# PROPER SUBSET
print(s2 < s1) # for example, s1 = {2, 4}, s2 = {2, 4}, s1 is not a proper subset of s2 because they both have same size and elems

# SUPERSET
print(s1 >= s2)

# PROPER SUPERSET
print(s1 > s2)

