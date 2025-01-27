from typing import List
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        direct_prerequisites = {c: 0 for c in range(numCourses)}
        dependants = {c: set() for c in range(numCourses)}

        for a, b in prerequisites:
            direct_prerequisites[b] += 1
            dependants[a].add(b)

        queue = deque(k for k, v in direct_prerequisites.items() if v == 0)
        
        all_prerequisites = {c: set() for c in range(numCourses)}
        while queue:
            c = queue.pop()
            for d in dependants[c]:
                all_prerequisites[d].update(all_prerequisites[c])
                all_prerequisites[d].add(c)
                direct_prerequisites[d] -= 1
                if direct_prerequisites[d] == 0:
                    queue.appendleft(d)
        
        ans = [None] * len(queries)
        for i, (a, b) in enumerate(queries):
            ans[i] = a in all_prerequisites[b]
        
        return ans
