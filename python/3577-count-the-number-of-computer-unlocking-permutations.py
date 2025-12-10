from math import perm

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if len(complexity) <= 1:
            return 1
        if any(c <= complexity[0] for c in complexity[1:]):
            return 0
        
        return perm(len(complexity) - 1, len(complexity) - 1) % (10**9 + 7)
