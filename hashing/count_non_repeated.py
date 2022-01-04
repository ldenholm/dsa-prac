def non_repeated(arr):
    #Your code here
    hash = {i : 0 for i in arr}
    for x in arr:
        hash[x] += 1
        # count how many items in dict have count 1
    print('printing hash', hash)
    print(sum([hash[i] for i in hash if hash[i] == 1]))
    #print(singly_occuring)
    #return sum(singly_occuring)
    

l1 = [1, 1, 2, 2, 2, 3, 4, 5]
print(non_repeated(l1))