from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = None
        b = None

        values = set(i + 1 for i in range(len(grid) * len(grid[0])))
        for row in grid:
            for v in row:
                if v not in values:
                    a = v
                else:
                    values.remove(v)
        if len(values) > 1:
            return None
        b = tuple(values)[0]
        return [a, b]

