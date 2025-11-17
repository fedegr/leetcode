# leetcode daily - 2025-11-17 - Check If All 1's Are at Least Length K Places Away

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = - k - 1
        for i, v in enumerate(nums):
            if v == 1:
                if i - last_one - 1 < k:
                    return False
                last_one = i
        return True
