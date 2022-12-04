class Solution:

    def minStartValue(self, nums: List[int]) -> int:
        # Construct a prefix sum
        ans = 0
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        # print(prefix)
        if min(prefix) <= 0: return abs(min(prefix)) + 1
        else: return 1
        
    # basically the answer has to be one greater than the minimum sum.
    # when there are only positive numbers then return min in the array