from math import comb
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mul = {}
        for i, a in enumerate(nums):
            for b in nums[i+1:]:
                m = a*b
                mul[m] = mul.get(m,0) + 1
        
        return sum([8 * comb(v, 2) for v in mul.values() if v > 1])
    