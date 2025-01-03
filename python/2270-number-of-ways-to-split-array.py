class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        >>> waysToSplitArray([1,1])
        1
        >>> waysToSplitArray([1,2])
        0
        >>> waysToSplitArray([10,4,-8,7])
        2
        >>> waysToSplitArray([2,3,1,0])
        2
        >>> waysToSplitArray([1,1,1,3])
        1
        """


        sums = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            sums[i+1] = sums[i] + nums[i]
        
        count = 0
        for i in range(1, len(sums) - 1):
            if sums[i] >= sums[-1] - sums[i]:
                count += 1
        
        return count