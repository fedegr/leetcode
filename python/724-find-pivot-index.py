class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i, n in enumerate(nums, 1):
            prefix_sum[i] = prefix_sum[i-1] + n
        
        for i in range(len(nums)):
            pre = prefix_sum[i]
            post = prefix_sum[-1] - prefix_sum[i+1]
            if pre == post:
                return i
        
        return -1
