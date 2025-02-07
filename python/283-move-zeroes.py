class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = 0
        while i < len(nums):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[i-zeros] = nums[i]
            i += 1
        
        for j in range(0, zeros):
            nums[-j-1] = 0

