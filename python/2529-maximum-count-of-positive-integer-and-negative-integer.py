from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_non_negative = bisect_left(nums, 0)
        negative_count = first_non_negative
        first_positive = bisect_right(nums, 0, lo=first_non_negative)
        positive_count = len(nums) - first_positive
        return max(negative_count, positive_count)
