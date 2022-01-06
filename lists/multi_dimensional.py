from array import *

def multi():
    multi = [[j for j in range(3)] for i in range (4)]
    print(multi)
    print(multi[0][2])

    arr1 = array('i', [1,2,3,4,5,6])
    print(arr1)

multi()