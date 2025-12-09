from collections import defaultdict
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        ans = 0

        num_right = defaultdict(lambda: 0)
        num_left = defaultdict(lambda: 0)
        for n in nums:
            num_right[n] += 1

        for n in nums:
            num_right[n] -= 1
            ans += (num_left[n*2] * num_right[n*2]) % mod
            num_left[n] += 1
            

        return ans % (mod)
    