def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            arr[i] = key
            i = i -1
    print('inside algo', arr)
    return arr

test = [31, 41, 59, 26, 41, 58]
insertion_sort(test)

# This version swaps the '>' in the while loop to '<'
# to sort in non-increasing order.
def insertion_sort_non_increasing_order(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] < key:
            arr[i+1] = arr[i]
            arr[i] = key
            i = i -1
    print('inside algo', arr)
    return arr

# Find a value v in a set of numbers size n, and
# return the index of v. Using a loop invariant 
# to prove the algorithm is correct.
def FindV(arr, v):
    # loop invariant
    v_is_found = False
    for i, num in enumerate(arr):
        if num == v:
            v_is_found = True
            return i
    return None