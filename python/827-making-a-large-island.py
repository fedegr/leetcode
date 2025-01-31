from collections import deque
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)
        island_size = [[(None, 0) for _ in range(width)] for _ in range(height)]
        ones = ((x, y) for y in range(height) for x in range(width) if grid[y][x] == 1)

        max_size = 0
        visited = set()
        for one in ones:
            if one in visited:
                continue
            island = set()
            queue = deque((one,))
            while queue:
                x, y = queue.pop()
                if (x, y) in island:
                    continue
                island.add((x,y))
                for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == 1:
                        queue.appendleft((nx, ny))
            
            for x, y in island:
                island_size[y][x] = (one, len(island))
            
            visited.update(island)
            
            if max_size < len(island):
                max_size = len(island)

        for x in range(width):
            for y in range(height):
                if grid[y][x] != 0:
                    continue
                size = 1
                islands = set()
                for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < width and 0 <= ny < height:
                        islands.add(island_size[ny][nx])

                size += sum(map(lambda x: x[1], islands))
                
                if max_size < size:
                    max_size = size
        
        return max_size
