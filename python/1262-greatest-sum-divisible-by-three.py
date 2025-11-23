class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum_best = (0, 0, 0)
        for n in nums:
            for b in tuple(sum_best):
                rest = (b + n) % 3
                sum_best[rest] = max(sum_best[rest], b + n)
        return sum_best[0]
