from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        steps = 0
        elems = sorted(e for row in grid for e in row)
        target = elems[len(elems) // 2]

        mod = elems[0] % x
        for i in range(len(elems)):
            if elems[i] % x != mod:
                return -1
            diff = abs(elems[i] - target)
            steps += diff // x

        return steps
