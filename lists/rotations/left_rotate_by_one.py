def rotate(arr):
    arr.append(arr[0])
    arr.pop(0)
    print(arr)
    # you can just use
    # arr.append(aa.pop(0))

l1 = [5, 10, 20 , 3]
rotate(l1)