from typing import Tuple


def smallest(prev: int, pattern: str, pattern_position: int, available: Tuple[int]):
    if len(pattern) == pattern_position:
        return ''
    
    best = None
    for n, free in enumerate(available):
        if not free:
            continue
        operation = pattern[pattern_position]
        if (operation == 'I' and prev > n) or (operation == 'D' and prev < n):
            continue
        
        available[n] = False
        val = smallest(n, pattern, pattern_position + 1, available)
        available[n] = True
        if val is None:
            continue
        val = str(n) + val
        print(pattern, prev, val)
        if best is None or val < best:
            best = val
        break
        
    return best


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        available = [True for _ in range(0, 10)]
        available[0] = False
        return smallest(0, 'I' + pattern, 0, available)
