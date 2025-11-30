from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0

        last_mod = {0: -1}
        prefix = 0
        smallest = len(nums)
        for i, n in enumerate(nums):
            prefix = (prefix + n) % p
            need = (prefix - target + p) % p
            smallest = min(smallest, i - last_mod.get(need, -smallest))
            last_mod[prefix] = i

        if smallest == len(nums):
            return -1

        return smallest
