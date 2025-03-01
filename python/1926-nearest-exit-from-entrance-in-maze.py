from typing import List, Tuple
from collections import deque


def next_positions(maze: List[List[str]], position: Tuple[int]):
    width = len(maze[0])
    height = len(maze)
    x, y = position
    return tuple(
        (x+dx, y+dy)
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1))
        if 0 <= x + dx < width and 0 <= y + dy < height and maze[y + dy][x + dx] == '.'
    )


def is_exit(maze: List[List[str]], position: Tuple[int]):
    width = len(maze[0])
    height = len(maze)
    x, y = position
    print(width, height, x, y, x == 0, x == width - 1, y == 0, y == height - 1)
    return x == 0 or x == width - 1 or y == 0 or y == height - 1


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        queue = deque()
        entrance = (entrance[1], entrance[0])
        queue.append((entrance, 0))

        while queue:
            pos, distance = queue.popleft()
            if pos in visited:
                continue
            if is_exit(maze, pos) and pos != entrance:
                return distance
            visited.add(pos)
            for next_pos in next_positions(maze, pos):
                queue.append((next_pos, distance + 1))
        
        return -1
