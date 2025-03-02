from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return None

        # value = None
        # heap = [-n for n in nums]
        # heapq.heapify(heap)
        # while k > 0:
        #     value = heapq.heappop(heap)
        #     k -= 1
        
        # return -value

        return heapq.nlargest(k, nums)[-1]
