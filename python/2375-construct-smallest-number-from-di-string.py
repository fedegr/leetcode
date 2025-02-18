from typing import Tuple


def smallest(prev: int, pattern: str, available: Tuple[int]):
    if len(pattern) == 0:
        return ''
    
    best = None
    for n in available:
        operation = pattern[0]
        if (operation == 'I' and prev > n) or (operation == 'D' and prev < n):
            continue
        
        val = smallest(n, pattern[1:], tuple(a for a in available if a != n))
        if val is None:
            continue
        val = str(n) + val
        # print(pattern, prev, val)
        if best is None or val < best:
            best = val
        break
        
    return best


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        available = tuple(n for n in range(1, 10))
        return smallest(0, 'I' + pattern, available)
