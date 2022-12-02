# Problem:
# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's 
# in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # We will use the sliding window technique with the following
        # constraint:
        
        # window breaks when window.count("0") > k
        # input [1,1,1,0,0,0,1,1,1,1,0], k = 2
        # ans = [1,1,1,0,0,1,1,1,1,1,1], length = 6
        
        # the length of the window is given by: right - left + 1
        
        left = ans = curr = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1 
            
            # curr = [1] 1, curr = 0
            # curr = [1,1] 2, curr = 0
            # curr = [1,1,1], curr = 0
            # curr = [1,1,1,0], curr = 1
            # curr = [1,1,1,0,0], curr = 2
            # curr = [1,1,1,0,0,0], curr = 3
            # curr = [1,1,1,0,0,0] 5
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
            
        return ans
                