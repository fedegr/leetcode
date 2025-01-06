from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_sum = 0
        values = [0]
        for i, n in enumerate(nums):
            if n == 0:
                values.append(0)
                if len(values) > k + 1:
                    values.pop(0)
            else:
                values[-1] += 1
            
            if max_sum < sum(values) + len(values) - 1:
                max_sum = sum(values) + len(values) - 1
        
        return max_sum
