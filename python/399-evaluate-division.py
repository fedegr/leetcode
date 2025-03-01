from typing import List
from collections import deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        relation = {}
        for (a, b), d in zip(equations, values):
            relation.setdefault(a, {}).setdefault(b, d)
            relation.setdefault(b, {}).setdefault(a, 1.0 / d)
        # for a in relation.keys():
        #     relation[a][a] = 1.0
        
        results = []
        for a, b in queries:
            if a not in relation or b not in relation:
                results.append(-1.0)
                continue
            
            answer = -1.0
            visited = set()
            queue = deque()
            queue.append((a, 1.0))
            while queue:
                current, value = queue.popleft()
                if current not in relation[a]:
                    relation[a][current] = value
                if current in visited:
                    continue
                visited.add(current)
                if current == b:
                    answer = value
                    break
                for n, v in relation[current].items():
                    queue.append((n, value * v))
            results.append(answer)

        return results