from collections import deque, defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        src = defaultdict(list)
        dest = defaultdict(list)

        for s, d in connections:
            src[d].append(s)
            dest[s].append(d)

        visited = set()
        queue = deque()
        queue.append(0)
        swaps = 0

        while queue:
            current = queue.popleft()
            visited.add(current)

            for d in dest[current]:
                if d not in visited:
                    queue.append(d)
                    swaps += 1
            
            for s in src[current]:
                if s not in visited:
                    queue.append(s)
        
        return swaps
