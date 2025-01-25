from collections import deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal_nodes = [None] * len(graph)

        def is_safe_node(node, path=tuple()) -> bool:
            if node in path or terminal_nodes[node] == False:
                for n in path:
                    terminal_nodes[n] = False
            
            if terminal_nodes[node] is None:
                terminal_nodes[node] = all(map(lambda x: is_safe_node(x, (*path, node)), graph[node]))
            
            return terminal_nodes[node]
                
        return [idx for idx in range(len(terminal_nodes)) if is_safe_node(idx)]
