class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Borrowing ideas from earlier we are given a sorted array
        # and the abs value of the first element once squared is potentiatlly
        # greater than the (n-1)th element.
        
        # Create array
        ans = []
        
        # Create two pointers
        i = 0
        j = len(nums) - 1
        
        # Start the loop at last item and decrement
        while i < j:
            if abs(nums[i]) > abs(nums[j]):
                # Greatest element so insert at the back of array
                ans.insert(0, nums[i] * nums[i])
                i += 1
            else:
                # Otherwise insert the nums[j]** value
                ans.insert(0, nums[j] * nums[j])
                j -= 1
            # Finish the new array by adding any remaining elements
        if i > j:
            ans.insert(0, nums[i] * nums[i])
        else:
            ans.insert(0, nums[j] * nums[j])
            
        # inp [-4,-1,0,3,10]
        # out [100,16,9,1]
        
        
                
        return ans