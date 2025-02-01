from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for n in arr:
            occurrences[n] = occurrences.get(n, 0) + 1
        
        return len(occurrences) == len(set(occurrences.values()))
