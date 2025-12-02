import math
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        ys = {}
        for x, y in points:
            ys.setdefault(y, set()).add(x)

        horizontal_lines = 0
        ys_combs = {}
        for y, xs in ys.items():
            if len(xs) >= 2:
                ys_combs[y] = math.comb(len(xs), 2)
                horizontal_lines += ys_combs[y]

        count = 0
        prev_parallel_lines = 0
        for y, combs in ys_combs.items():
            horizontal_lines -= combs
            count += (combs * horizontal_lines)

        return count % (10**9 + 7)
