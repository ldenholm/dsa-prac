def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        print("current: ", arr)
        upper = [i for i in arr[1:] if i > pivot]

        lower = [i for i in arr[1:] if i <= pivot]
        print("lower = ", lower, "upper = ", upper, "pivot = ", pivot)

        return quicksort(lower) + [pivot] + quicksort(upper)

l1 = [4, 0, 2, 1]
l2 = [1, 5, 10, 2, -1, -17, 48, 96]
print(quicksort(l1))
print(quicksort(l2))