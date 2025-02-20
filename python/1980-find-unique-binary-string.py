from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = sorted(int(num, 2) for num in nums)

        answer = n
        for i, num in enumerate(nums):
            if i != num:
                answer = i
                break
        
        return ("{0:0" + str(n) + "b}").format(answer)