from typing import List
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        

        adjacents = {
            i: tuple(j for j in range(len(isConnected)) if i != j and isConnected[i][j] == 1)
            for i in range(len(isConnected))
        }
        
        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            provinces += 1
            stack = deque()
            stack.append(i)

            while stack:
                current = stack.pop()
                if current in visited:
                    continue
                visited.add(current)

                for neighbour in adjacents[current]:
                    stack.append(neighbour)
        return provinces
