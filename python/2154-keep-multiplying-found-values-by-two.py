from bisect import bisect_left

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        i = 0
        i = bisect_left(nums, original, i, len(nums))
        while i < len(nums) and nums[i] == original:
            original *= 2
            i = bisect_left(nums, original, i, len(nums))
        return original
