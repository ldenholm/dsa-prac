def is_sorted_ascending_order(arr):
    n = len(arr)
    print(n)
    # check if list empty or contains 1 element
    if n in [0, 1]:
        return True
    first = arr[0]
    for i in range(1, n):
        if arr[i] > first:
            return True
        elif arr[i] < first:
            return False

l1 = [10, 20, 30]
l2 = [10, 20, 20, 30]
l3 = [10, 5, 2]

print(is_sorted_ascending_order(l1))
print(is_sorted_ascending_order(l2))
print(is_sorted_ascending_order(l3))