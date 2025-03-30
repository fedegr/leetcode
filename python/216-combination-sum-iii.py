from typing import List
from collections import deque


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
        - Only numbers 1 through 9 are used.
        - Each number is used at most once.
        """

        combinations = {}
        stack = deque()
        stack.append((1, k, n, False))

        while(stack):
            start, size, total_sum, collect = stack.pop()

            if (start, size, total_sum) in combinations:
                continue

            if size == 1:
                if total_sum == start:
                    combinations[(start, size, total_sum)] = ((start,),)
                continue

            if collect:
                combinations[(start, size, total_sum)] = tuple(
                    (start, *c)
                    for i in range(start+1, 10)
                    for d in (0, 1)
                    for c in combinations.get((i, size - d, total_sum - start * d), tuple())
                    if sum(c) + start == total_sum
                )
            else:
                stack.append((start, size, total_sum, True))
                for i in range(start + 1, 10):
                    if i <= total_sum:
                        stack.append((i, size, total_sum, False))
                    if i <= total_sum - start:
                        stack.append((i, size - 1, total_sum - start, False))

        return tuple(
            c 
            for start in range(1, 10)
            for c in combinations.get((start, k, n), [])
        )
