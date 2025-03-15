from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = 0, max(nums)
        def can_rob_k_houses(capacity):
            robbed_houses, i = 0, 0
            while i < len(nums):
                if nums[i] <= capacity:
                    robbed_houses += 1
                    if robbed_houses == k:
                        return True
                    i += 1
                i += 1
            return False

        min_capacity = None
        while left <= right:
            mid = (left + right) // 2
            if can_rob_k_houses(mid):
                min_capacity = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return min_capacity
