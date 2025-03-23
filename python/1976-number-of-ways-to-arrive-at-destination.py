from typing import List
from collections import defaultdict, namedtuple
from functools import cache
from math import inf

Neighbour = namedtuple("Neighbour", ['node', 'distance'])


mod = 10 ** 9 + 7

@cache
def count_paths(previous_nodes, node) -> int:
    if len(previous_nodes[node]) == 0:
        return 1
    
    return sum(
        count_paths(previous_nodes, n) 
        for n in previous_nodes[node]
    ) % mod
    

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        neighbours = defaultdict(list)

        for n1, n2, d in roads:
            neighbours[n1].append(Neighbour(n2, d))
            neighbours[n2].append(Neighbour(n1, d))

        root_distance = defaultdict(lambda: inf)
        root_distance[0] = 0
        previous = defaultdict(list)
        unvisited = set(i for i in range(n))

        while unvisited:
            current = min(unvisited, key=lambda x: root_distance[x])
            unvisited.remove(current)

            for node, distance in neighbours[current]:
                if root_distance[current] + distance > root_distance[node]:
                    continue
                elif root_distance[current] + distance < root_distance[node]:
                    root_distance[node] = root_distance[current] + distance
                    previous[node] = [current]
                else:
                    previous[node].append(current)
        
        previous = tuple(tuple(previous[i]) for i in range(n))

        return count_paths(previous, n - 1)
