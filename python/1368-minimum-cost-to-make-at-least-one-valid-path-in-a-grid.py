from typing import List

RIGHT = 1
LEFT = 2
DOWN = 3
UP = 4

sign_direction = {
    RIGHT: (1, 0),
    LEFT: (-1,0),
    DOWN: (0, 1),
    UP: (0, -1),
}


def walk(grid, position, visited=None):
    x, y = position
    if visited is None:
        visited = set()
    while 0 <= y < len(grid) and 0 <= x < len(grid[0]) and (x, y) not in visited:
        visited.add((x, y))
        sign = grid[y][x]
        dx, dy = sign_direction[sign]
        x, y = x+dx, y+dy
    return visited


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        visited = [ [False for _ in row] for row in grid]
        changes = 0
        current = walk(grid, (0,0))

        while (len(grid[0]) - 1, len(grid) - 1) not in current:
            next_cells = set()
            changes += 1
            for (x, y) in current:
                if visited[y][x]:
                    continue
                visited[y][x] = True
                
                for dx, dy in sign_direction.values():
                    if 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]) and not visited[y + dy][x + dx]:
                        next_cells.update(walk(grid, (x+dx, y+dy), next_cells))
            current = next_cells
        
        return changes

