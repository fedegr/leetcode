from typing import List
import heapq

FIRST_GROUP = 0
LAST_GROUP = 1

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        group_position = {
            FIRST_GROUP: 0,
            LAST_GROUP: len(costs) - 1
        }
        for i in range(candidates):
            for group in (FIRST_GROUP, LAST_GROUP):
                if group_position[FIRST_GROUP] > group_position[LAST_GROUP]:
                    continue
                pos = group_position[group] 
                heapq.heappush(heap, (costs[pos], pos, group))
                group_position[group] += 1 if group == FIRST_GROUP else -1

        total_cost = 0
        for k_ in range(k):
            c, _, group = heapq.heappop(heap)
            total_cost += c
            if group_position[FIRST_GROUP] > group_position[LAST_GROUP]:
                continue
            
            pos = group_position[group]
            heapq.heappush(heap, (costs[pos], pos, group))
            group_position[group] += 1 if group == FIRST_GROUP else -1
        
        return total_cost
