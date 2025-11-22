from functools import reduce
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return reduce(lambda acc, n: acc + min(n % 3, 3 - n % 3), nums, 0)
