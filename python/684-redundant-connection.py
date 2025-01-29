from collections import deque
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connection = {}

        for n1, n2 in edges:
            connection.setdefault(n1, set())
            connection.setdefault(n2, set())
            connection[n1].add(n2)
            connection[n2].add(n1)

        loop = None
        stack = deque(((1, tuple()),))
        visited = set()
        while stack:
            node, path = stack.pop()
            if node in visited:
                loop_node, loop = node, path
                break

            visited.add(node)
            
            for adjacent in connection[node]:
                n1, n2 = sorted([node, adjacent])
                if len(path) > 0 and (n1, n2) == path[-1]:
                    continue
                stack.append((adjacent, (*path, (n1, n2))))
        
        if loop is None:
            return None

        cycle_start = None
        count = 0
        for i, (n1, n2) in enumerate(path):
            if (n1 == loop_node or n2 == loop_node):
                if cycle_start is None:
                    cycle_start = i 
                count += 1
        
        if count == 3:
            path = path[cycle_start+1:]

        for n1, n2 in reversed(edges):
            if (n1, n2) in path:
                return (n1, n2)
        
        return None
    