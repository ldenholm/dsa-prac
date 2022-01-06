def bsearch_recursive(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if x == arr[mid]:
        return mid
    elif x > arr[mid]:
        low = mid + 1
        return bsearch_recursive(arr, x, low, high)
    elif x <= arr[mid]:
        high = mid - 1
        return bsearch_recursive(arr, x, low, high)

t0 = [2, 4, 6, 8]
print(bsearch_recursive(t0, 2, 0, len(t0)-1))
print(bsearch_recursive(t0, 8, 0, len(t0)-1))
print(bsearch_recursive(t0, 6, 0, len(t0)-1))
print(bsearch_recursive(t0, 4, 0, len(t0)-1))
print(bsearch_recursive(t0, 10, 0, len(t0)-1))