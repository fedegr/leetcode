from bisect import bisect_left

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        theoretical_max = sum(batteries) // n
        
        def can_run(x):
            capacity_needed = x * n
            capacity = 0
            for b in batteries:
                capacity += min(x, b)
            return capacity >= capacity_needed

        low, high = 0, theoretical_max
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can_run(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
