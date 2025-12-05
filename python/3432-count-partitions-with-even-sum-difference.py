class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix_sum = [0]*len(nums)

        prefix_sum[0] = nums[0]
        for i, n in enumerate(nums[1:], start=1):
            prefix_sum[i] = prefix_sum[i-1] + n
        
        count = 0
        for i in range(len(nums) - 1):
            if (prefix_sum[-1] - prefix_sum[i]) % 2 - (prefix_sum[i] % 2) == 0:
                count += 1
                
        return count
