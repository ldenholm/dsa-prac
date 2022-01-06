def binary_search(arr, x):
    n = len(arr) - 1
    lower = 0
    mid = (lower + n) // 2
    i = 0
    while lower <= n:
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            lower = mid + 1
            mid = (lower + n) // 2
        elif x <= arr[mid]:
            n = mid - 1
            mid = (lower + n) // 2
    return -1

 #    0     m    n-1
 #    0  1  2  3  4
t0 = [1, 2, 3, 4, 5]
#t1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 2
print(binary_search(t0, 4))
print(binary_search(t0, 5))