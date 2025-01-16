from typing import List
from functools import reduce

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        
        result = 0
        if len(nums1) % 2 == 1:
            result ^= reduce(lambda x, y: x ^ y, nums2, 0)

        if len(nums2) % 2 == 1:
            result ^= reduce(lambda x, y: x ^ y, nums1, 0)

        return result
