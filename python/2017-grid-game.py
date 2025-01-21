from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row1sum = [0] * (len(grid[0]) + 1)
        for x, val in enumerate(grid[0]):
            row1sum[x+1] = row1sum[x] + val

        row2sum = [0] * (len(grid[0]) + 1)
        for x, val in enumerate(grid[1]):
            row2sum[x+1] = row2sum[x] + val

        best = None
        for pos in range(len(grid[0])):
            new = max(
                row1sum[-1] - row1sum[pos+1] if pos + 1 < len(row1sum) else 0,
                row2sum[pos],
            )
            if best is None or new < best:
                best = new
        return best
        