class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        hashmap = set(nums)

        for i in range(len(nums)):

            if i not in hashmap:

                return i

            elif len(nums) not in hashmap:

                return len(nums)

           

            # input [0, 1] => expected output = 2