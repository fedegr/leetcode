from collections import deque
from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_fishes = 0
        water_cells = list((x,y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] > 0)

        visited = set()
        for start in water_cells:
            if start in visited:
                continue
            fishes = 0
            queue = deque((start,))
            while queue:
                cx, cy = queue.popleft()
                if (cx, cy) in visited:
                    continue
                visited.add((cx, cy))
                fishes += grid[cy][cx]
                if max_fishes < fishes:
                    max_fishes = fishes
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = cx + dx, cy + dy
                    if (
                        nx < 0 or len(grid[0]) <= nx or
                        ny < 0 or len(grid) <= ny or
                        grid[ny][nx] == 0
                    ):
                        continue
                    queue.append((nx, ny))

        return max_fishes
                    
