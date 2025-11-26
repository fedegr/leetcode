from collections import deque, defaultdict
from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        w, h = len(grid[0]), len(grid)
        mod = 10**9 + 7
        path_count = [[defaultdict(lambda: 0) for _ in range(w)] for _ in range(h)]
        path_count[0][0] = {grid[0][0] % k: 1}

        for x in range(1, w):
            for sum_, paths in path_count[0][x-1].items():
                val = (grid[0][x] + sum_) % k
                path_count[0][x][val] = paths % mod
        
        for y in range(1, h):
            for sum_, paths in path_count[y-1][0].items():
                val = (grid[y][0] + sum_) % k
                path_count[y][0][val] = paths % mod

        for y in range(1, h):
            for x in range(1, w):
                for nx, ny in ((x - 1, y), (x, y - 1)):
                    for sum_, paths in path_count[ny][nx].items():
                        val = (grid[y][x] + sum_) % k
                        path_count[y][x][val] = (path_count[y][x][val] + paths) % mod
        
        return path_count[-1][-1].get(0, 0)


    def numberOfPathsStack(self, grid: List[List[int]], k: int) -> int:
        w, h = len(grid[0]), len(grid)
        mod = 10**9 + 7
        path_count = [[None for _ in range(w)] for _ in range(h)]        
        
        stack = deque()
        for nx, ny in ((1, 0), (0, 1),):
            if nx >= w or ny >= h or path_count[ny][nx] is not None:
                continue
            stack.appendleft((nx, ny))

        path_count[0][0] = {grid[0][0] % k: 1}

        while stack:
            x, y = stack.pop()
            path_count[y][x] = defaultdict(lambda: 0)
            current_val = grid[y][x] % k
            for nx, ny in ((x - 1, y), (x, y - 1)):
                if nx < 0 or ny < 0: 
                    continue
                for sum_, paths in path_count[ny][nx].items():
                    val = (current_val + sum_) % k
                    path_count[y][x][val] = (path_count[y][x][val] + paths) % mod

            for nx, ny in ((x + 1, y), (x, y + 1)):
                if nx >= w or ny >= h or path_count[ny][nx] is not None:
                    continue
                stack.appendleft((nx, ny))
            
        # self.print_paths(path_count)
        
        return path_count[-1][-1].get(0, 0)
    
    def print_paths(self, path_count):
        lines = []
        for row in path_count:
            line = []
            lines.append(line)
            for cell in row:
                line.append(f"{dict(cell)}")
        
        # print("\n".join(" ".join(l) for l in lines))
        max_row = tuple(max(len(row[c]) for _, row in enumerate(lines)) for c in range(len(lines[0])))
        for line in lines:
            # print(" ".join(col for c, col in enumerate(line)))
            print(" ".join(col.rjust(max_row[c], " ") for c, col in enumerate(line)))