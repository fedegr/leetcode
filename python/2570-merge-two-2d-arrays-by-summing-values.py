class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        answer = []
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):

            if i < len(nums1):
                id_i, val_i = nums1[i]
            else:
                id_i, val_i = nums2[-1][0] + 1, 0

            if j < len(nums2):
                id_j, val_j = nums2[j]
            else:
                id_j, val_j = nums1[-1][0] + 1, 0
            
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
        
        return answer
