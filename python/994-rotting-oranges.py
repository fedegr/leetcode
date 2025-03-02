from typing import List, Tuple
from collections import deque

EMPTY = 0
FRESH = 1
ROTTEN = 2


def next_positions(matrix: List[List[str]], position: Tuple[int]):
    width = len(matrix[0])
    height = len(matrix)
    x, y = position
    return tuple(
        (x+dx, y+dy)
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1))
        if 0 <= x + dx < width and 0 <= y + dy < height
    )


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

        i = 0
        while fresh and rotten:
            queue = deque(rotten)
            rotten = []

            while queue:
                current = queue.popleft()

                for neighbour in next_positions(grid, current):
                    nx, ny = neighbour
                    if grid[ny][nx] == FRESH:
                        rotten.append(neighbour)
                        fresh.remove(neighbour)
                        grid[ny][nx] = ROTTEN
            
            i += 1

        if fresh:
            return -1

        return i 
