from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # let's do the O(n^2) solution, we have quadratic time because
    # we use two loops.
    for i in range(len(nums)-1):
        # [1, 2 ,4, 5, 6] 
        #  i -> -> .       first loop starts nums[i] until one len(nums)-1

        for j in range(i + 1, len(nums)):
            # second loop:
            # [1, 2 ,4, 5, 6]
            #     j -> -> ->   starts nums[i+1] goes until end

            # next compare nums[j] + nums[i] = target?
            if nums[i] + nums[j]:
                # we need to return list of indexes, so we can do that like so:
                return [i, j]

    # to visualize things the loops running together look like this:
    #-----i=0--------
    # [1, 2 ,4, 5, 6]
    # [i -> -> ->, -]
    # [-  j -> -> ->]
    #-----i=1--------
    # [1, 2 ,4, 5, 6]
    # [-  i -> ->, -]
    # [-  -  j -> ->]
    #-----i=2--------
    # [1, 2 ,4, 5, 6]
    # [-  -  i ->, -]
    # [-  -  - j ->]
    #-----i=3--------
    # [1, 2 ,4, 5, 6]
    # [-  -  -  i  -]
    # [-  -  -  -  j]
