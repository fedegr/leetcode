from typing import List
from collections import defaultdict


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        repetitions = defaultdict(lambda: 0)
        for n in nums:
            repetitions[n] += 1
        
        return all(map(lambda x: x % 2 == 0, repetitions.values()))