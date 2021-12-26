def avg(list):
    avg = 0
    for i in list:
        avg += i
    return avg/len(list)

testOne = [10, 20, 30, 40]
testTwo = [30, 60, 40]
print(avg(testOne))
print(avg(testTwo))