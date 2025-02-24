from collections import deque
from typing import Dict, List, Optional, Tuple


def dfs(
    adjacents: Dict[int, List[int]],
    amount: List[int],
    bob: Dict[int, int],
) -> Tuple[List[int], int]:
    visited = set()
    stack = deque()
    stack.append((0, 0, 0))

    best = None
    while stack:
        current, step, profit = stack.pop()
        bob_step = bob.get(current, None)

        if current in visited:
            continue
        visited.add(current)

        if bob_step is None or bob_step > step:
            profit += amount[current]
        elif bob_step == step:
            profit += amount[current] // 2
        
        neighbours = adjacents.get(current, [])
        for neighbour in neighbours:
            stack.append((neighbour, step+1, profit))

        if len(neighbours) == 1 and neighbours[0] in visited and (best is None or profit > best):
            best = profit

    return best


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjacents = {}
        for i, j in edges:
            adjacents.setdefault(i, []).append(j)
            adjacents.setdefault(j, []).append(i)

        bob_path = {}
        def calculate_bob_path_global(
            current: int,
            step: int,
            parent: Optional[int] = None,
        ) -> Tuple[List[int], int]:
            if current == 0:
                bob_path[current] = step
                return True
            
            for neighbour in adjacents[current]:
                if neighbour == parent:
                    continue
                
                if calculate_bob_path(neighbour, step+1, current):
                    bob_path[current] = step
                    return True

            return False

        def calculate_bob_path(
            current: int,
            step: int,
            parent: Optional[int] = None,
        ) -> Dict[int, int]:
            if current == 0:
                return {current: step}
            
            for neighbour in adjacents[current]:
                if neighbour == parent:
                    continue
                
                path = calculate_bob_path(neighbour, step+1, current)
                if path:
                    path[current] = step
                    return path

            return None
        
        bob_path = calculate_bob_path(bob, 0)

        return dfs(adjacents, amount, 0, bob=bob_path)

