from typing import List
from math import sqrt
from bisect import bisect_left


def can_repair_cars(ranks: List[int], cars: int, minutes: int) -> bool:
    max_cars = sum(int(sqrt(minutes // rank)) for rank in ranks)
    return max_cars >= cars


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        return bisect_left(
            range(1, ranks[0] * cars * cars),
            True,
            key=lambda x: can_repair_cars(ranks, cars, x),
        ) + 1
