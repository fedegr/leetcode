from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        is_rotated = False

        prev = nums[0]
        for n in nums[1:]:
            if prev > n:
                if is_rotated:
                    return False
                is_rotated = True
            prev = n
        
        return not is_rotated or nums[-1] <= nums[0]
