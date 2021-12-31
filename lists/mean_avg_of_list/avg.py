def avg(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

testOne = [10, 20, 30, 40]
testTwo = [30, 60, 40]
print(avg(testOne))
print(avg(testTwo))

def mean_concice(arr):
    return sum(arr)/len(arr)

print(mean_concice(testOne))