from collections import defaultdict, deque
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(set)
        for n1, n2 in edges:
            connections[n1].add(n2)
            connections[n2].add(n1)
        
        complete = 0
        checked = set()
        for node in range(n):
            if node in checked:
                continue

            is_complete = True
            component_nodes = connections[node] | set([node])
            for neighbor in connections[node]:
                if connections[neighbor] | set([neighbor]) != component_nodes:
                    is_complete = False
                    break

            checked.update(component_nodes)
            
            if is_complete:
                complete += 1
            
        return complete 
