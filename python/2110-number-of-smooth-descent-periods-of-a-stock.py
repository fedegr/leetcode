from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        descent_periods = 0

        current_size = 1
        prev = prices[0]
        for v in prices[1:] + [None]:
            if v == prev -1:
                current_size += 1
            else:
                descent_periods += (current_size * (current_size+1)) // 2
                current_size = 1
            prev = v

        return descent_periods
