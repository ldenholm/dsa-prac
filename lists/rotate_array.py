def rotate(arr, d, n):
    temp = arr[:d]
    new = arr[d:]
    new.append(temp)
    print(temp)
    print(new)
    for i in range(n, ):
        temp = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = temp
    print('orig after left shift', arr)

l = [1,2,3,4,5]
rotate(l, 2, 5)