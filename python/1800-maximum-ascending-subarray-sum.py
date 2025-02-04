from collections import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        answer = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                s += nums[i]
            else:
                if answer < s:
                    answer = s
                s = nums[i]
        
        if answer < s:
            answer = s
        
        return answer
        
                