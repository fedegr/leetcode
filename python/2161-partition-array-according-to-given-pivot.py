from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pre_pivot, pivots, post_pivot = [], [], []

        for n in nums:
            if n < pivot:
                pre_pivot.append(n)
            elif n > pivot:
                post_pivot.append(n)
            else:
                pivots.append(n)
        
        return [*pre_pivot, *pivots, *post_pivot]