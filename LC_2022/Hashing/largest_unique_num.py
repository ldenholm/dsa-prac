from ast import List
from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # you can create a hash to map nums to frequency
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        nums_appearing_once = [v for v in freq_map if freq_map[v] == 1]
        if len(nums_appearing_once) > 0:
            return max(nums_appearing_once)
        else:
            return -1