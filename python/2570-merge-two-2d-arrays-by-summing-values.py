from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        answer = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            id_i, val_i = nums1[i]
            id_j, val_j = nums2[j]
            if id_i < id_j:
                next_id, next_val = id_i, val_i
                i += 1
            elif id_i > id_j:
                next_id, next_val = id_j, val_j
                j += 1
            else:
                next_id, next_val = id_i, val_i + val_j
                i += 1
                j += 1
            answer.append([next_id, next_val])
        
        while i < len(nums1):
            answer.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            answer.append(nums2[j])
            j += 1
        
        return answer
