def count_distinct(arr):
    s = set()
    s.update(arr)
    return len(s)

l1 = [10, 20, 10, 30, 30, 20]
print(count_distinct(l1))

# even more concise version
def count_disctinct_better(arr):
    return len(set(arr))

print(count_disctinct_better(l1))