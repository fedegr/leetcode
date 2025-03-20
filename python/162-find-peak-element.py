from math import inf


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            prev_val = -inf if i == 0 else nums[i - 1]
            next_val = -inf if i == len(nums) - 1 else nums[i + 1]

            if prev_val < nums[i] and next_val < nums[i]:
                return i
        return -1
            