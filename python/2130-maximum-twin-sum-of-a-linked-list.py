from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional["ListNode"]) -> int:
        n = 0
        node = head
        while node is not None:
            node = node.next
            n += 1

        half = n // 2
        arr = [0] * half
        i = 0
        node = head
        
        while node is not None:
            if i < half:
                arr[i] = node.val
            else:
                arr[n - i - 1] += node.val
            node = node.next
            i += 1
        
        return max(arr)

        
        