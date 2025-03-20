from typing import List
from math import ceil


def can_eat_all_bananas(piles, h, k):
    time = 0
    for bananas in piles:
        time += ceil(bananas / k)
        if time > h:
            return False
    return True


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1
        if h == len(piles):
            return max(piles)
        left = 1
        right = max(piles)
        while left < right:
            center = (left + right) // 2
            if can_eat_all_bananas(piles, h, center):
                right = center
            else:
                left = center + 1
        return right