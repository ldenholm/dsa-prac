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

#using append + pop:
def rotate_by_k_builtin(arr, k):
    for i in range(0, k):
        arr.append(arr.pop(0))
    print(arr)

l2 = [2, 4, 5, 6]
rotate_by_k_builtin(l2, 3)

# using O(n) time, and O(1) space:
#def best_rotate(arr, k):