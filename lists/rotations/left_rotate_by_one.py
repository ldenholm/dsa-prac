def rotate(arr):
    arr.append(arr[0])
    arr.pop(0)
    print(arr)
    # you can just use
    # arr.append(aa.pop(0))

l1 = [5, 10, 20 , 3]
#rotate(l1)

# using a loop
def rotate_loop(arr):
    last = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr [i]
        print(arr)
    arr[len(arr)-1] = last
    print(arr)

rotate_loop(l1)