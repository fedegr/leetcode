from typing import List
from collections import deque

EMPTY = 0
FRESH = 1
ROTTEN = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = [
            (x,y) 
            for y, row in enumerate(grid) 
            for x, orange in enumerate(row)
            if orange == ROTTEN
        ]
        fresh = set(
            (x,y) 
            for y, row in enumerate(grid) 
            for x, orange in enumerate(row)
            if orange == FRESH
        )
        width = len(grid[0])
        height = len(grid)


        i = 0
        while fresh and rotten:
            queue = deque(rotten)
            rotten = []

            while queue:
                x, y = queue.popleft()
                fresh_neighbours = tuple(
                    (x+dx, y+dy)
                    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1))
                    if 0 <= x + dx < width and 0 <= y + dy < height and grid[y+dy][x+dx] == FRESH
                )

                for neighbour in fresh_neighbours:
                    nx, ny = neighbour
                    rotten.append(neighbour)
                    fresh.remove(neighbour)
                    grid[ny][nx] = ROTTEN
            
            i += 1

        if fresh:
            return -1

        return i 
