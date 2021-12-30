def sum(arr):
    if len(arr) < 2:
        return arr[0]
    else:
        return arr.pop() + sum(arr)
l1 = [1, 2, 3, 7, 10]
print(sum(l1))