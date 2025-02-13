from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional["TreeNode"]) -> int:
        if root is None:
            return 0
        longest_zig_zag = 0
        stack = deque(((root, None, 0),))
        while len(stack):
            current, last_direction, size = stack.pop()

            if current is None:
                continue
            
            if longest_zig_zag < size:
                longest_zig_zag = size
            
            for next_direction, child in ((0, current.left), (1, current.right)):                
                stack.append((child, next_direction, size + 1 if last_direction != next_direction else 1 ))
        
        return longest_zig_zag