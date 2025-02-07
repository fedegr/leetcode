from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if head is None or head.next is None:
            return None
        
        node = head
        size = 1
        while node.next is not None:
            node = node.next
            size += 1

        node = head
        prev = None
        steps = size // 2
        while steps > 0:
            prev = node
            node = node.next
            steps -= 1
        
        if prev is None:
            return head.next

        prev.next = prev.next.next
        return head
