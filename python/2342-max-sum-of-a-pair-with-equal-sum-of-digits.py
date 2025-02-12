from typing import List
import heapq


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = {}
        for n in nums:
            ds = sum(int(c) for c in str(n))
            numbers_with_ds = digit_sum.setdefault(ds, list())
            if len(numbers_with_ds) <= 1:
                heapq.heappush(numbers_with_ds, n)
            else:
                heapq.heappushpop(numbers_with_ds, n)

        
        best = -1
        for ds, numbers in digit_sum.items():
            if len(numbers) <= 1:
                continue
            s = numbers[0] + numbers[1]
            if best < s:
                best = s

        return best
