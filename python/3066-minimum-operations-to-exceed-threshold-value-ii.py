from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops = 0
        while len(nums) >= 2 and nums[0] < k:
            x = heapq.heappop(nums)
            y = nums[0]
            heapq.heappushpop(nums, x * 2 + y)
            ops += 1
        return ops