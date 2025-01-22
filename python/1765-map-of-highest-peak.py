from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque([
            (x,y, 0)
            for y in range(len(isWater))
            for x in range(len(isWater[0]))
            if isWater[y][x] == 1
        ])

        visited = set()

        while len(queue) > 0:
            x, y, height = queue.popleft()

            if (x, y) in visited:
                continue
            
            isWater[y][x] = height
            visited.add((x,y))
            for dx, dy in ((1,0), (-1,0), (0,1), (0, -1)):
                nx, ny = x+dx, y+dy
                if (0 <= nx < len(isWater[0]) and 
                    0 <= ny < len(isWater) and
                    (nx, ny) not in visited
                ):
                    queue.append((nx, ny, height+1))
        
        return isWater
