from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 1
        size = 1
        sign = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 0:
                sign = 0
                size = 1
                continue

            diff //= abs(diff)
        
            if sign == diff or sign == 0:
                size += 1
            else:
                size = 2
            sign = diff
                    
            if size > longest:
                longest = size
        
        return longest

