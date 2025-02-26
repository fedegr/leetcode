from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best = 0
        current_positive = 0
        current_negative = 0
        for n in nums:
            current_positive += n
            if current_positive < 0:
                current_positive = 0
            elif best < current_positive:
                best = current_positive

            current_negative += n
            if current_negative > 0:
                current_negative = 0
            elif best < -current_negative:
                best = -current_negative
        return best
