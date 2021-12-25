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
#print(test)
