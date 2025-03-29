from typing import List
from collections import defaultdict


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)        
        for n in nums:
            counter[n] += 1

        dominant, dominant_repetitions = max(counter.items(), key=lambda x: x[1])
        first_half_count = 0
        for i, n in enumerate(nums):
            if n == dominant:
                first_half_count += 1
                if (
                    first_half_count > (i + 1) // 2 and 
                    (dominant_repetitions - first_half_count) > (len(nums) - i - 1) // 2
                ):
                    return i
        
        return -1
        