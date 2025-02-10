from typing import Optional
from collections import namedtuple

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if head is None:
            return head
        
        current = head
        odds = head
        evens_start = namedtuple('StartNode', ['next'])
        evens = evens_start
        is_odd = True
        while current is not None:
            next_node = current.next
            if is_odd:
                odds.next = current
                odds = odds.next
                odds.next = None
            else:
                evens.next = current
                evens = evens.next
                evens.next = None
            current = next_node
            is_odd = not is_odd
        
        if odds is not None:
            odds.next = evens_start.next

        return head
