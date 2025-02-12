from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_digit_sum = {}
        best = -1
        for n in nums:
            ds, tmp = 0, n
            while tmp:
                ds += tmp % 10
                tmp //= 10

            if ds not in max_digit_sum:
                max_digit_sum[ds] = n
            else:
                if best < max_digit_sum[ds] + n:
                    best = max_digit_sum[ds] + n
                max_digit_sum[ds] = max(max_digit_sum[ds], n)

        return best
