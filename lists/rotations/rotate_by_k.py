def rotate_by_k(arr, k):
    for i in range(k):
        rotate(arr)
    print(arr)

def rotate(arr):
    n = len(arr)
    first = arr[0]
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n-1] = first
    return arr
    
l1 = [10, 5, 6, 4]
k = 2
rotate_by_k(l1, k)