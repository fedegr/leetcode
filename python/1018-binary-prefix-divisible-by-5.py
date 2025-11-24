class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        prefix = 0
        result = [None] * len(nums)
        for i, b in enumerate(nums):
            prefix = ((prefix << 1) | b) % 5
            result[i] = prefix == 0
        return result
