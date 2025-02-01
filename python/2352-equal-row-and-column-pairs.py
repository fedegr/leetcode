# 2352-equal-row-and-column-pairs
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:        
        rows = {}
        cols = {}
        for j, row in enumerate(grid):
            row = tuple(row)
            rows[row] = rows.get(row, 0) + 1
            col = tuple(grid[i][j] for i in range(len(grid)))
            cols[col] = cols.get(col, 0) + 1
        
        answer = 0
        for col, rep in cols.items():
            answer += rep * rows.get(col, 0)

        return answer
