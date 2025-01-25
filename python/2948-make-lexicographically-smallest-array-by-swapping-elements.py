from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        numpos = sorted((n, i) for i, n in enumerate(nums))

        answer = [None] * len(nums)
        group_start = 0
        for i, (n, _) in enumerate(numpos[1:], 1):
            if n > numpos[i-1][0] + limit:
                positions = sorted(map(lambda x: x[1], numpos[group_start:i]))
                for j, p in enumerate(positions):
                    answer[p] = numpos[group_start + j][0]
                group_start = i
        
        positions = sorted(map(lambda x: x[1], numpos[group_start:]))
        for j, p in enumerate(positions):
            answer[p] = numpos[group_start + j][0]

        return answer

