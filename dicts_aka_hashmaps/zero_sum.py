def zero_sum(arr):
    # use prefix sum
    # traverse array and compute prefix sum, add it to hash table, if sum already in hash table then return True
    prefix_sum = 0
    hash = set()
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == 0 or prefix_sum in hash:
            # already exists
            return True
        hash.add(prefix_sum)
    return False

l1 = [-3, 4, -3, -1, 1]
l2 = [5, 4, 1, -10]
print(zero_sum(l1))
print(zero_sum(l2))