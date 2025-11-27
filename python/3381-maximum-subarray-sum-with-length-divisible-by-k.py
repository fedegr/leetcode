from typing import List
from math import inf

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_prefix_sum = [inf] * k
        min_prefix_sum[k-1] = 0
        prefix_sum, best = 0, -inf
        for i, num in enumerate(nums):
            prefix_sum += num
            mod = i % k
            best = max(best, prefix_sum - min_prefix_sum[mod])
            min_prefix_sum[mod] = min(min_prefix_sum[mod], prefix_sum)
        return best
