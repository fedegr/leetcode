from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        best = 0
        best_sum = 0
        min_heap = []
        
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        for n2, n1 in pairs:
            best_sum += n1
            if len(min_heap) < k:
                heapq.heappush(min_heap, n1)
            else:
                best_sum -= heapq.heappushpop(min_heap, n1)
            current = best_sum * n2
            if len(min_heap) == k and current > best:
                best = current
        return best
