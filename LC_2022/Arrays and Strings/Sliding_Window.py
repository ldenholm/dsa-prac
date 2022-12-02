class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Use a window strategy with the following constraint
        # window.length = k
        
        curr = ans = 0
        
        for i in range(k):
            # create a window of size 4
            curr += nums[i]
            # current represents sum of window of size k
        # our answer is the mean (sum / k) dont divide by k here, we can do it in the final return
        ans = curr / k
        
        # now we test the rest of the array to see if larger means exist
        for i in range(k, len(nums)):
            
            
            curr += nums[i] - nums[i - k]
            
            
            ans = max(ans, (curr / k))
        return ans