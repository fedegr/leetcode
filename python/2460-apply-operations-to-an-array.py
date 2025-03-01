from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        first_zero = None
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if first_zero is not None:
                if nums[i] == 0:
                    continue
                nums[first_zero], nums[i] = nums[i], nums[first_zero]
                first_zero += 1
            elif nums[i] == 0:
                first_zero = i
        if first_zero is not None:
            nums[first_zero], nums[-1] = nums[-1], nums[first_zero]
            first_zero += 1
        
        return nums
