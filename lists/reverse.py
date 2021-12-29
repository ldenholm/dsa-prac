def reverse(list):
    n = len(list) - 1
    for i in range(n):
        if n - i > i:
            temp = list[i]
            list[i] = list[n-i]
            list[n-i] = temp
            print(list)

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 6, 8, 4, 5]
reverse(l1)
# 1 < 4 - 1
print('original l2: ', l2)
reverse(l2)

# lets try just a size 3 list
l3 = [1, 3, 5]
print('original l2: ', l3)
reverse(l3)