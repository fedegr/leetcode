from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited_count = 0
        queue = deque()
        queue.append(0)
        
        while queue:
            room = queue.popleft()
            if visited[room]:
                continue
            visited[room] = True
            visited_count += 1
            for r in rooms[room]:
                queue.append(r)
        
        return visited_count == len(rooms)
