from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if head is None:
            return head
        
        reversed_list = head
        current = head.next
        reversed_list.next = None

        while current is not None:
            current.next, reversed_list, current = reversed_list, current, current.next

        return reversed_list