from math import comb

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # bad = 0
        # for i, ni in enumerate(nums):
        #     for j, nj in enumerate(nums[i+1:], i+1):
        #         if j - i != nj - ni:
        #             bad += 1
        # return bad

        total = comb(len(nums), 2)
        diff = {}
        for i, ni in enumerate(nums):
            d = ni - i
            diff[d] = diff.get(d, 0) + 1
        
        good = 0
        for c in diff.values():
            good += comb(c, 2)
            
        return total - good