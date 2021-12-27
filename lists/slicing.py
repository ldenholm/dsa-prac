def slicing(arr, d):
    # rotate arr by d
    for i in range(d):
        arr.append(arr[i])
        arr[i] = arr[i+1]
    return arr

l = [1, 2, 3, 4, 5]
d = 2
#l = l[:d]
#new.append(l[:d])
print(l)
#print(l[:d])

print(slicing(l, d))