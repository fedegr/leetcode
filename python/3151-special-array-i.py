from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        last_is_even = nums[0] % 2
        for n in nums[1:]:
            is_even = n % 2
            if is_even == last_is_even:
                return False
            last_is_even = is_even

        return True
