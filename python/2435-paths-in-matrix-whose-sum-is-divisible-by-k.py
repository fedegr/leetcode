from collections import deque, defaultdict

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        w, h = len(grid[0]), len(grid)
        mod = 10**9 + 7
        prev_sums = None
        sums = [{} for _ in range(w+1)]
        sums[1] = {0: 1}

        for y in range(0, h):
            prev_sums = sums
            sums = [{} for _ in range(w+1)]
            for x in range(0, w):
                for prev_cell in (prev_sums[x+1], sums[x]):
                    for sum_, paths in prev_cell.items():
                        val = (grid[y][x] + sum_) % k
                        sums[x+1][val] = (sums[x+1].get(val, 0) + paths) % mod
        return sums[-1].get(0,0)
