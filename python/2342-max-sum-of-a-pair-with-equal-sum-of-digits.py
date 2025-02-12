from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = {}
        for n in nums:
            ds = sum(int(c) for c in str(n))
            digit_sum.setdefault(ds, list()).append(n)
        
        best = -1
        for ds, numbers in digit_sum.items():
            if len(numbers) <= 1:
                continue
            s = sum(sorted(numbers, reverse=True)[:2])
            if best < s:
                best = s

        return best
    