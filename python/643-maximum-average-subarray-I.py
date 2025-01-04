class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])

        best = s
        for i in range(1, len(nums) - k + 1):
            s = s + nums[i + k - 1] - nums[i - 1]
            best = max(s, best)
        
        return float(best) / k
    