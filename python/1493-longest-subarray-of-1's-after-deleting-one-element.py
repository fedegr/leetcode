class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        first_group = 0
        second_group = 0
        deletion = False
        has_zero = False
        longest = 0

        for i, n in enumerate(nums):
            if n == 0:
                has_zero = True
                if deletion:
                    first_group = second_group
                    second_group = 0
                else:
                    deletion = True
            else:
                if deletion:
                    second_group += 1
                else:
                    first_group += 1

            if longest < first_group + second_group:
                longest = first_group + second_group
                    
        return longest - (0 if has_zero else 1)
