def binary_search(arr, x):
    # n = last index in array
    n = len(arr) - 1
    lower = 0
    mid = n // 2
    print(n)
    print(mid)
    i = 0
    #for i in range(len(arr)):
    while i < len(arr):
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            lower = mid + 1
            mid = (lower + n) // 2
        elif x <= arr[mid]:
            n = mid - 1
            mid = (lower + n) // 2
        i += 1
    return -1

 #    0     m    n-1
t0 = [1, 2, 3, 4, 5]
#t1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 2
print(binary_search(t0, 4))