from typing import List
import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        grid = tuple(tuple(row) for row in grid)
        queries = sorted(enumerate(queries), key=lambda x: x[1])
        print(list([idx, val] for idx, val in queries if val > 999000))
        
        visited = set()
        priority_queue = [(grid[0][0], (0, 0))]
        points = 0
        idx = 0
        result = [None] * len(queries)

        while len(priority_queue) > 0 and idx < len(queries):
            value, pos = heapq.heappop(priority_queue)
            if pos in visited:
                continue
            visited.add(pos)

            while idx < len(queries) and value >= queries[idx][1]:
                result[queries[idx][0]] = points
                idx += 1
            
            if idx == len(queries):
                break
            
            points += 1
            (x, y) = pos

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if not (0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)):
                    continue
                heapq.heappush(priority_queue, (grid[y+dy][x+dx], (x+dx, y+dy)))
        
        while idx < len(queries):
            result[queries[idx][0]] = points
            idx += 1

        return result
