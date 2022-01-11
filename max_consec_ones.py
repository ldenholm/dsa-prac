from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    # treat it like a string, with 0 as the delimeter
    # create string array
    x = ""
    for i in nums:
        x += str(i)
    final = x.split('0')
    print(final)
    max = 0
    for j in final:
        if (max<len(j)):
            max = len(j)

list = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(list))


def sortedSquares(nums: List[int]) -> List[int]:
    squared = []
    for x in nums:
        squared.append(x * x)
    squared.sort()
        