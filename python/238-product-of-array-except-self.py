class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeros = 0
        prod = 1
        for n in nums:
            if n == 0:
                zeros += 1
                continue
            prod *= n
        
        if zeros > 0:
            for i in range(len(nums)):
                nums[i] = prod if nums[i] == 0 and zeros == 1 else 0
        else:
            for i in range(len(nums)):
                nums[i] = prod // nums[i]
        
        return nums
