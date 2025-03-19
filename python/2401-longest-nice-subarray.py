from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        best = 1
        curr_len = 0
        curr_val = 0

        for i in range(len(nums)):
            while curr_len >= 1 and (curr_val & nums[i]) != 0:
                curr_val -= nums[i - curr_len]
                curr_len -= 1

            curr_len += 1
            curr_val |= nums[i]
            if best < curr_len:
                best = curr_len

        return best