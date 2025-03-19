from typing import List


def flip(b):
    return 0 if b == 1 else 1


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                flips += 1
                nums[i] = 1
                nums[i+1] = flip(nums[i+1])
                nums[i+2] = flip(nums[i+2])
        
        return flips if nums[-1] == 1 and nums[-2] == 1 else -1