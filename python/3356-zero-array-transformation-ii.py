from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        changes = [0] * (len(nums) + 1)
        
        k = 0
        decrement = 0
        for i, n in enumerate(nums):

            while decrement + changes[i] < n and k < len(queries):
                l, r, v = queries[k]
                if i <= r:
                    changes[max(i, l)] += v
                    changes[r+1] -= v
                k += 1
            decrement += changes[i]

            if decrement < n and k == len(queries):
                return -1

        return k
