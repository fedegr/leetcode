from bisect import bisect_left

def can_split(candies, candies_per_child, children_count):
    if candies_per_child == 0:
        return True
    return sum([c // candies_per_child for c in candies]) >= children_count


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        min_split, max_split = 0, sum(candies) // k
        while min_split <= max_split:
            mid = (min_split + max_split) // 2
            if can_split(candies, mid, k):
                min_split = mid + 1
            else:
                max_split = mid - 1

        return max_split
        